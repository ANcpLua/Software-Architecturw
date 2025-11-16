"""Mars Moon Visibility Calculator - Application Core"""

from collections.abc import Iterable
from dataclasses import dataclass

# ===== Shared Mars time constants (AS1) =====

MARS_MINUTES_PER_HOUR: int = 100
MARS_MINUTES_PER_DAY: int = 25 * MARS_MINUTES_PER_HOUR  # 2500

# ===== Data structures =====

Interval = tuple[int, int]


@dataclass(frozen=True)
class TimeWindow:
    """A single Mars visibility window expressed in Mars hours/minutes."""
    start_h: int
    start_m: int
    end_h: int
    end_m: int


@dataclass(frozen=True)
class ParsedWindows:
    """Output of component A: structured Deimos and Phobos time windows."""
    deimos: TimeWindow
    phobos: TimeWindow


@dataclass(frozen=True)
class NormalizedWindows:
    """Output of component B: windows converted to day-relative minute intervals."""
    deimos_intervals: list[Interval]
    phobos_intervals: list[Interval]


@dataclass(frozen=True)
class OverlapResult:
    """Output of component C: total overlap duration in Mars-minutes."""
    minutes: int


# ===== Component A: TimeWindowParser =====

class TimeWindowParser:
    """Component A: parse 8 integers into two structured time windows."""
    __slots__ = ()

    def parse(self, values: Iterable[int]) -> ParsedWindows:
        """Parse 8 integers into structured time windows for Deimos and Phobos."""
        vals = list(values)
        if len(vals) != 8:
            raise ValueError(f"Expected 8 integers, got {len(vals)}")

        d_start_h, d_start_m, d_end_h, d_end_m, p_start_h, p_start_m, p_end_h, p_end_m = vals

        return ParsedWindows(
            deimos=TimeWindow(d_start_h, d_start_m, d_end_h, d_end_m),
            phobos=TimeWindow(p_start_h, p_start_m, p_end_h, p_end_m),
        )


# ===== Component B: TimeWindowNormalizer =====

class TimeWindowNormalizer:
    """Component B: convert TimeWindows to day-relative Mars-minute intervals.

    Intervals are half-open [start, end) in the domain [0, 2500).
    Windows that cross midnight are split into two intervals.
    """
    __slots__ = ()

    def normalize(self, windows: ParsedWindows) -> NormalizedWindows:
        """Normalize both Deimos and Phobos windows."""
        return NormalizedWindows(
            deimos_intervals=self._normalize_single(windows.deimos),
            phobos_intervals=self._normalize_single(windows.phobos),
        )

    @staticmethod
    def _to_minutes(hour: int, minute: int) -> int:
        """Convert Mars timestamp (hour 0-25, minute 0-99) to minutes since midnight."""
        return (hour * MARS_MINUTES_PER_HOUR + minute) % MARS_MINUTES_PER_DAY

    def _normalize_single(self, window: TimeWindow) -> list[Interval]:
        """Normalize a single time window, handling wraparound cases."""
        start = self._to_minutes(window.start_h, window.start_m)
        end = self._to_minutes(window.end_h, window.end_m)

        if start == end:
            return [(0, MARS_MINUTES_PER_DAY)]

        if start < end:
            return [(start, end)]

        # Wraparound: split into [start, 2500) and [0, end) if end > 0
        intervals = [(start, MARS_MINUTES_PER_DAY)]
        if end > 0:
            intervals.append((0, end))
        return intervals


# ===== Component C: OverlapCalculator =====

class OverlapCalculator:
    """Component C: compute geometric overlap of two sets of intervals."""
    __slots__ = ()

    def calculate(self, windows: NormalizedWindows) -> OverlapResult:
        """Calculate total overlap between Deimos and Phobos intervals."""
        total_minutes = 0

        for d_start, d_end in windows.deimos_intervals:
            for p_start, p_end in windows.phobos_intervals:
                start = max(d_start, p_start)
                end = min(d_end, p_end)

                if end > start:
                    overlap = end - start
                    total_minutes += overlap

        return OverlapResult(minutes=total_minutes)


# ===== Component D: DurationExtractor (Twilight Rule) =====

class DurationExtractor:
    """Component D: extract final joint visibility duration.

    Returns overlap in minutes, or 1 if intervals share a boundary (Twilight Rule).
    """
    __slots__ = ()
    TWILIGHT_MINUTES: int = 1

    def extract(self, overlap: OverlapResult, windows: NormalizedWindows) -> int:
        """Extract visibility duration, applying Twilight Rule if needed."""
        if overlap.minutes > 0:
            return overlap.minutes

        # Check Twilight Rule: do intervals share a boundary in circular time?
        points_deimos = self._boundary_points(windows.deimos_intervals)
        points_phobos = self._boundary_points(windows.phobos_intervals)

        if points_deimos & points_phobos:
            return self.TWILIGHT_MINUTES

        return 0

    @staticmethod
    def _boundary_points(intervals: Iterable[Interval]) -> set[int]:
        """Extract boundary points normalized to circular time (0 ≡ 2500)."""
        points: set[int] = set()
        for start, end in intervals:
            points.add(start % MARS_MINUTES_PER_DAY)
            points.add(end % MARS_MINUTES_PER_DAY)
        return points


# ===== Public application core API =====

_parser = TimeWindowParser()
_normalizer = TimeWindowNormalizer()
_overlap_calculator = OverlapCalculator()
_duration_extractor = DurationExtractor()


def moon(
        D_start_h: int,
        D_start_m: int,
        D_end_h: int,
        D_end_m: int,
        P_start_h: int,
        P_start_m: int,
        P_end_h: int,
        P_end_m: int,
) -> int:
    """Calculate joint visibility of Deimos and Phobos in Mars-minutes.

    Returns total overlap in minutes, or 1 if windows share a boundary.
    """
    parsed = _parser.parse([
        D_start_h, D_start_m, D_end_h, D_end_m,
        P_start_h, P_start_m, P_end_h, P_end_m,
    ])
    normalized = _normalizer.normalize(parsed)
    overlap = _overlap_calculator.calculate(normalized)
    return _duration_extractor.extract(overlap, normalized)


# ===== Examples =====

if __name__ == "__main__":
    print("Example 1: D[13:91, 23:05], P[22:05, 24:45] ->", moon(13, 91, 23, 5, 22, 5, 24, 45))
    print("Example 2: D[24:53, 7:12],  P[5:12, 8:45]   ->", moon(24, 53, 7, 12, 5, 12, 8, 45))
    print("Example 3: D[12:32, 17:06], P[17:06, 19:78] ->", moon(12, 32, 17, 6, 17, 6, 19, 78))
    print("Example 4: D[5:00, 6:00],    P[7:00, 8:00]  ->", moon(5, 0, 6, 0, 7, 0, 8, 0))
    print("Example 5: D[10:00, 25:00],  P[0:00, 5:00]  ->", moon(10, 0, 25, 0, 0, 0, 5, 0))

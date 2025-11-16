# Mars Moons Application Core

**Exercise ID:** Mars02

**Related Exercises:**

- [Charts/Products Architecture Analysis](../../Evening 2 - Architectural Quality/07-charts-products-architecture-story/architectural-principles-analysis.md)
- [Climate Model Analysis](../../Evening 2 - Architectural Quality/08-climate-model-architecture-analysis/climate-model-analysis.md)

---

> Quick start for Rider/PyCharm users is at the end of this file.

## 1. Goal of the Application Core

We want a **very small application core** for the Mars experiment software.

- The core receives **eight integers** representing two Mars‑intervals:  
  one for **Deimos**, one for **Phobos** (REQ1).
- The core returns **one integer**:  
  the number of **Mars‑minutes** during which both moons are visible (REQ2).
- If the intervals share exactly one boundary point, the result must be **1 minute**  
  (“Twilight Rule”, REQ3).
- On Earth, this core can be used by a simple **non‑GUI interface** for testing (REQ4).
- **Input validation is not part of the application core** – it assumes valid Mars timestamps (per the exercise
  statement).

The architecture consists of **four very small cohesive components** that use each other in a strict linear pipeline:

```text
A  -->  B  -->  C  -->  D
```

Where:

- **A**: TimeWindowParser
- **B**: TimeWindowNormalizer
- **C**: OverlapCalculator
- **D**: DurationExtractor (Twilight Rule)

The public core function is:

```text
Moon(D_start_h, D_start_m, D_end_h, D_end_m,
     P_start_h, P_start_m, P_end_h, P_end_m) -> int
```

This function is implemented as `moon(...)` in the Python file below.

---

## 2. Mars Time System & Assumptions (AS1–AS6)

### AS1 – Simplified Mars Time

We adopt the simplified Mars time system:

- 1 sol (Mars day) = **25** Mars hours
- 1 Mars hour = **100** Mars minutes
- 1 sol = **2500** Mars‑minutes

Valid timestamps:

- Hours: `0–25` (where `25:00` is the same instant as `0:00` of the next sol).
- Minutes: `0–99`.

We convert a Mars timestamp `(hour, minute)` to minutes since midnight using:

```text
M(hour, minute) = (hour * 100 + minute) mod 2500
```

This gives a value in the range `[0, 2499]`.

### AS2 & AS3 – Mars Intervals and Midnight Crossing

Each moon has one visibility interval per sol:

```text
D = [D_rise, D_set]
P = [P_rise, P_set]
```

Both endpoints are Mars timestamps.

- Intervals may **cross midnight**.  
  Example: `[24:44, 7:50]` – the moon rises at 24:44 on the current sol and sets at 7:50 the next sol.
- After conversion to minutes:
    - If `end >= start` → the interval is inside the same sol.
    - If `end < start` → the interval wraps to the next sol.

In our model, we treat intervals as **half‑open**: `[start, end)`.  
This is standard for time ranges and matches the overlap arithmetic used in the core.

### AS4 – Mid‑Minute Events

We assume a moon rises and sets exactly in the **middle of a Mars‑minute**.  
Therefore, representing time as discrete minutes is sufficient and we never need fractions.

### AS5 – Same Interval Pattern Across Days

Assumption AS5 states that if an interval is valid for a given sol, it is also valid for the previous and next sol.  
Our normalization uses this by:

- Splitting wraparound intervals into `[start, 2500)` and `[0, end)`, and
- Keeping all calculations within a single “reference” sol `[0, 2500)`.

### AS6 – No GUI on Mars

On Mars, the `Moon` function is called by NASA’s **coordination software**, not via a GUI.  
On Earth, we can wrap the core in a simple **text‑based interface** (command line or script) for testing (REQ4).  
The core itself has **no GUI dependencies**.

---

## 3. Core Architecture: Four Components A–D

### Overview Table

| Component ID | Component Name       | One‑sentence job description                                                                             | Input data (example)                                          | Output data (example)                                                              |
|--------------|----------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------|
| **A**        | TimeWindowParser     | Parse 8 integers into two structured Mars visibility windows (Deimos & Phobos).                          | `D[13:91, 23:05] P[22:05, 24:45]` → `[13,91,23,5,22,5,24,45]` | `ParsedWindows { deimos: TimeWindow(13,91,23,5), phobos: TimeWindow(22,5,24,45) }` |
| **B**        | TimeWindowNormalizer | Convert Mars timestamps to minutes since midnight and normalize intervals, handling midnight wraparound. | `ParsedWindows` from A                                        | `NormalizedWindows { deimos: [(1391,2305)], phobos: [(2205,2445)] }`               |
| **C**        | OverlapCalculator    | Compute the total geometric overlap (in minutes) between the Deimos and Phobos minute intervals.         | `NormalizedWindows` from B                                    | `OverlapResult { interval: (2205,2305), minutes: 100 }`                            |
| **D**        | DurationExtractor    | Convert overlap information to the final integer minutes, applying the Twilight Rule when needed.        | `OverlapResult` from C + `NormalizedWindows` from B           | `100` (or `1` in a twilight case; REQ2 & REQ3)                                     |

---

## 4. Developer setup (Rider/PyCharm)

The code is pure Python and depends only on the standard library (no third‑party packages).

- Python version: 3.14 recommended (3.12+ required for modern type syntax)
- Working folder: `Mars/03-mars-moons-application-core`

Two shared Run/Debug configurations are included in version control under `Mars/.run/`:

- "Mars Moon Core" – runs `mars_moon_core.py` and prints five sample scenarios
- "Mars Moon Core Tests" – runs `test_mars_moon_core.py` with unittest

Follow these steps once per machine:

1. Open the solution folder `Mars` in Rider or PyCharm.
2. Configure a Python SDK for the project/module:
   - Preferences/Settings → Python Interpreter → Add
   - Choose your local Python 3.14 (or 3.12+) or create a new Virtualenv.
   - If you already have a venv under this folder (e.g., `03-mars-moons-application-core/venv`), you can select it.
3. Select one of the shared run configurations from the Run/Debug dropdown:
   - Run "Mars Moon Core" to see example outputs matching the problem statement.
   - Run "Mars Moon Core Tests" to execute the full unit test suite.

One-time automatic interpreter setup (no manual clicks):

From the repository root, run once to create a dedicated venv for this solution folder:

```bash
# from repo root
python3 setup-python-venv.py Mars/03-mars-moons-application-core
# or (if executable):
./setup-python-venv Mars/03-mars-moons-application-core
```

After that you can either:
- Activate it in any terminal: `source Mars/03-mars-moons-application-core/venv/bin/activate`
- Or in Rider/PyCharm: set the interpreter to `Mars/03-mars-moons-application-core/venv/bin/python3`

Command line alternatives:

```bash
cd Mars/03-mars-moons-application-core
python3 -m unittest -v test_mars_moon_core.py
python3 mars_moon_core.py
```

> Tip: from the repository root you can now run `python mars_moon_core.py`.  
> The wrapper at the top level automatically jumps into this directory, ensures
> the dedicated virtual environment exists, and launches the script for you.

Troubleshooting:

- If you see "Please specify a Python SDK", open Project/Module settings and select the Python interpreter (step 2 above).
- No requirements need to be installed; the `requirements.txt` is intentionally empty because we use only the stdlib.

### 3.1 Component A – TimeWindowParser

**Responsibility:**  
Split the 8 input integers into two typed `TimeWindow` objects.  
No time calculations, no validation – just **shaping** data.

- **Input:**  
  `[D_start_h, D_start_m, D_end_h, D_end_m, P_start_h, P_start_m, P_end_h, P_end_m]`  
  Example: `[13, 91, 23, 5, 22, 5, 24, 45]`
- **Output:**  
  `ParsedWindows` containing:
    - `deimos = TimeWindow(13, 91, 23, 5)`
    - `phobos = TimeWindow(22, 5, 24, 45)`

---

### 3.2 Component B – TimeWindowNormalizer

**Responsibility:**  
Apply Mars time semantics (AS1–AS3) and normalize each window into one or two minute intervals:

1. Convert each timestamp to minutes:
   ```text
   start = M(start_h, start_m)
   end   = M(end_h,   end_m)
   ```
2. Interpret `[start, end)` as follows:
    - If `start == end` → full sol visible → `[(0, 2500)]`.
    - If `start < end` → simple interval in the same sol → `[(start, end)]`.
    - If `start > end` → wraparound → `[(start, 2500), (0, end)]`.

Examples:

- `D[14:00, 22:40]` → `[(1400, 2240)]`.
- `P[24:44, 7:50]` → `[(2444, 2500), (0, 750)]`.
- `D[24:53, 7:12]` → `[(2453, 2500), (0, 712)]`.

All intervals lie inside the half‑open domain `[0, 2500)`.

---

### 3.3 Component C – OverlapCalculator

**Responsibility:**  
Compute the **geometric** overlap of the two sets of intervals.

- For each pair of intervals `(di, pj)`:
  ```text
  overlap_start = max(di.start, pj.start)
  overlap_end   = min(di.end,   pj.end)
  overlap       = max(0, overlap_end - overlap_start)
  ```
- Sum `overlap` over all pairs → total overlap minutes.
- Also compute a canonical overlap interval `[start, start + minutes)` (or `None` if total overlap is 0) mainly for
  clarity; the final result in D is still the total minutes.

Examples:

- `deimos: [(1391,2305)]`, `phobos: [(2205,2445)]` → overlap `[2205,2305)` → 100 minutes.
- `deimos: [(2453,2500),(0,712)]`, `phobos: [(512,845)]` → overlap `[512,712)` → 200 minutes.

---

### 3.4 Component D – DurationExtractor (Twilight Rule)

**Responsibility:**  
Convert the overlap result into the final integer minutes by applying REQ2 and REQ3:

1. **Non‑zero overlap:**
    - If `overlap.minutes > 0` → return that value directly (REQ2).
2. **Zero overlap → Twilight Rule check:**
    - Build boundary sets in **circular time**, normalizing with `t % 2500`:
      ```text
      points_Deimos = { (start % 2500), (end % 2500) for each Deimos interval }
      points_Phobos = { (start % 2500), (end % 2500) for each Phobos interval }
      ```
    - If `points_Deimos ∩ points_Phobos` is non‑empty → return `1` (REQ3).
    - Otherwise → return `0`.

This definition:

- Matches the case‑study twilight examples, and
- Also treats 0 and 2500 as the **same point** for Twilight purposes, so an interval ending at 2500 and another starting
  at 0 share a boundary point in circular time.

---

## 4. Per‑Component Test Cases

See the tables in section 3 (A/B/C/D) – they can be used directly as unit test inputs and expected outputs.

End‑to‑end tests for the public `moon(...)` function should include:

- REQ2 examples:
    - `moon(13,91,23,5,22,5,24,45) == 100`
    - `moon(24,53,7,12,5,12,8,45) == 200`
- REQ3 examples:
    - `moon(12,32,17,6,17,6,19,78) == 1`
    - `moon(22,11,0,36,7,0,22,11) == 1`
- No‑overlap case:
    - `moon(5,0,6,0,7,0,8,0) == 0`
- Midnight twilight case (circular boundary):
    - Deimos: `[10:00, 25:00]`, Phobos: `[0:00, 5:00]` → geometric overlap 0 but shared boundary at midnight →
      `moon(10,0,25,0,0,0,5,0) == 1`.

---

## 5. Single‑File Python Implementation (Application Core)

```python name=mars_moon_core.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple

# ===== Shared Mars time constants (AS1) =====

MARS_MINUTES_PER_HOUR: int = 100
MARS_MINUTES_PER_DAY: int = 25 * MARS_MINUTES_PER_HOUR  # 2500


# ===== Data structures =====

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


Interval = Tuple[int, int]  # (start_minute, end_minute), 0 <= start < end <= 2500


@dataclass(frozen=True)
class NormalizedWindows:
    """Output of component B: windows converted to day-relative minute intervals."""
    deimos_intervals: List[Interval]
    phobos_intervals: List[Interval]


@dataclass(frozen=True)
class OverlapResult:
    """
    Output of component C: geometric overlap interval, if any.

    If there is no geometric overlap (i.e., the intersection is empty),
    `interval` is None and `minutes` is 0.
    """
    interval: Optional[Interval]
    minutes: int


# ===== Component A: TimeWindowParser =====

class TimeWindowParser:
    """
    Component A: parse 8 integers into two structured time windows.

    This component assumes its inputs are valid per the Mars case study.
    It performs *no* validation by design.
    """

    def parse(self, values: Iterable[int]) -> ParsedWindows:
        vals = list(values)
        if len(vals) != 8:
            # Defensive check, not domain-level validation.
            raise ValueError(f"Expected 8 integers, got {len(vals)}")
        (
            d_start_h,
            d_start_m,
            d_end_h,
            d_end_m,
            p_start_h,
            p_start_m,
            p_end_h,
            p_end_m,
        ) = vals

        deimos = TimeWindow(d_start_h, d_start_m, d_end_h, d_end_m)
        phobos = TimeWindow(p_start_h, p_start_m, p_end_h, p_end_m)
        return ParsedWindows(deimos=deimos, phobos=phobos)


# ===== Component B: TimeWindowNormalizer =====

class TimeWindowNormalizer:
    """
    Component B: convert TimeWindows to day-relative Mars-minute intervals.

    Responsibilities:
    - Apply the simplified Mars time system (AS1).
    - Implement wraparound semantics (AS2, AS3).
    - Represent each window as either:
        - a single interval [(start, end)], or
        - two intervals [(start, 2500), (0, end)] if it crosses midnight, or
        - [(0, 2500)] if the moon is visible for a full sol (start == end).

    Intervals are modeled as half-open [start, end) in the domain [0, 2500).
    """

    def normalize(self, windows: ParsedWindows) -> NormalizedWindows:
        d = self._normalize_single(windows.deimos)
        p = self._normalize_single(windows.phobos)
        return NormalizedWindows(deimos_intervals=d, phobos_intervals=p)

    @staticmethod
    def _to_minutes(hour: int, minute: int) -> int:
        """
        Convert a Mars timestamp to minutes since midnight.

        This assumes `hour` and `minute` are valid:
        - hour: 0–25, where 25:00 wraps to 0:00
        - minute: 0–99
        """
        total = hour * MARS_MINUTES_PER_HOUR + minute
        return total % MARS_MINUTES_PER_DAY

    def _normalize_single(self, window: TimeWindow) -> List[Interval]:
        start = self._to_minutes(window.start_h, window.start_m)
        end = self._to_minutes(window.end_h, window.end_m)

        # Full-day interval: visible all sol (AS5 is implicitly respected)
        if start == end:
            return [(0, MARS_MINUTES_PER_DAY)]

        # Simple case: no wraparound
        if start < end:
            return [(start, end)]

        # Wraparound: split into [start, 2500) and [0, end)
        return [(start, MARS_MINUTES_PER_DAY), (0, end)]


# ===== Component C: OverlapCalculator =====

class OverlapCalculator:
    """
    Component C: compute geometric overlap of two sets of intervals.

    - Intervals are in [0, 2500), non-empty (start < end).
    - Returns the total overlap and a canonical overlap interval (if any).
      The canonical interval is [start, start + minutes) where `start` is the
      earliest overlap start; it is only used as a convenient representation
      for component D.
    """

    def calculate(self, windows: NormalizedWindows) -> OverlapResult:
        deimos = windows.deimos_intervals
        phobos = windows.phobos_intervals

        total_minutes = 0
        first_overlap_start: Optional[int] = None

        for d_start, d_end in deimos:
            for p_start, p_end in phobos:
                start = max(d_start, p_start)
                end = min(d_end, p_end)
                if end > start:
                    overlap = end - start
                    total_minutes += overlap
                    if first_overlap_start is None or start < first_overlap_start:
                        first_overlap_start = start

        if total_minutes == 0 or first_overlap_start is None:
            return OverlapResult(interval=None, minutes=0)

        return OverlapResult(
            interval=(first_overlap_start, first_overlap_start + total_minutes),
            minutes=total_minutes,
        )


# ===== Component D: DurationExtractor (Twilight Rule) =====

class DurationExtractor:
    """
    Component D: extract final joint visibility duration in minutes.

    - If there is a non-zero geometric overlap, return it unchanged (REQ2).
    - If there is no geometric overlap but the intervals share at least one
      boundary point (in circular Mars time), return 1 (Twilight Rule, REQ3).
    - Otherwise return 0.
    """

    TWILIGHT_MINUTES: int = 1

    def extract(self, overlap: OverlapResult, windows: NormalizedWindows) -> int:
        if overlap.minutes > 0:
            return overlap.minutes

        # No geometric overlap; check Twilight Rule in circular time (0 ≡ 2500).
        points_deimos = self._boundary_points(windows.deimos_intervals)
        points_phobos = self._boundary_points(windows.phobos_intervals)
        if points_deimos & points_phobos:
            return self.TWILIGHT_MINUTES

        return 0

    @staticmethod
    def _boundary_points(intervals: Iterable[Interval]) -> set[int]:
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
    """
    Application core entry point (REQ1–REQ3).

    Input (REQ1):
        Four timestamps for Deimos and four for Phobos, given as 8 integers:
        D_start_h, D_start_m, D_end_h, D_end_m,
        P_start_h, P_start_m, P_end_h, P_end_m

    Output (REQ2, REQ3):
        One integer: total minutes of joint visibility, including Twilight Rule.

    Input validation is NOT part of this application core: we assume the
    8 integers satisfy AS1–AS3 (valid Mars timestamps and intervals).
    """
    parsed = _parser.parse(
        [
            D_start_h,
            D_start_m,
            D_end_h,
            D_end_m,
            P_start_h,
            P_start_m,
            P_end_h,
            P_end_m,
        ]
    )
    normalized = _normalizer.normalize(parsed)
    overlap = _overlap_calculator.calculate(normalized)
    result = _duration_extractor.extract(overlap, normalized)
    return result


# ===== Minimal Earth-side HCI for manual testing (REQ4) =====

if __name__ == "__main__":
    # Example from REQ2: 100 minutes (22:05 to 23:05)
    print("Example 1: D[13:91, 23:05], P[22:05, 24:45] ->", moon(13, 91, 23, 5, 22, 5, 24, 45))

    # Wraparound example from REQ2: 200 minutes (5:12 to 7:12)
    print("Example 2: D[24:53, 7:12],  P[5:12, 8:45]   ->", moon(24, 53, 7, 12, 5, 12, 8, 45))

    # Twilight rule example: single boundary point -> 1 minute
    print("Example 3: D[12:32, 17:06], P[17:06, 19:78] ->", moon(12, 32, 17, 6, 17, 6, 19, 78))

    # No overlap, no twilight
    print("Example 4: D[5:00, 6:00],    P[7:00, 8:00]  ->", moon(5, 0, 6, 0, 7, 0, 8, 0))

    # Midnight twilight example: D[10:00, 25:00], P[0:00, 5:00] -> 1 (circular midnight boundary)
    print("Example 5: D[10:00, 25:00],  P[0:00, 5:00]  ->", moon(10, 0, 25, 0, 0, 0, 5, 0))
```

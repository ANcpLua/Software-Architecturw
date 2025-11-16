"""
Comprehensive test suite for mars_moon_core.py

Tests all components (A, B, C, D) individually and the integrated moon() function.
"""

import unittest

from mars_moon_core import (
    moon,
    TimeWindowParser,
    TimeWindowNormalizer,
    OverlapCalculator,
    DurationExtractor,
    TimeWindow,
    ParsedWindows,
    NormalizedWindows,
    OverlapResult,
    MARS_MINUTES_PER_DAY,
)


class TestTimeWindowParser(unittest.TestCase):
    """Test Component A: TimeWindowParser"""

    def setUp(self):
        self.parser = TimeWindowParser()

    def test_parse_valid_input(self):
        """Test parsing 8 integers into structured windows."""
        result = self.parser.parse([13, 91, 23, 5, 22, 5, 24, 45])
        self.assertEqual(result.deimos, TimeWindow(13, 91, 23, 5))
        self.assertEqual(result.phobos, TimeWindow(22, 5, 24, 45))

    def test_parse_invalid_count(self):
        """Test that parsing rejects non-8 integer inputs."""
        with self.assertRaises(ValueError):
            self.parser.parse([1, 2, 3])

    def test_parse_midnight_timestamps(self):
        """Test parsing midnight-related timestamps."""
        result = self.parser.parse([0, 0, 25, 0, 0, 0, 5, 0])
        self.assertEqual(result.deimos, TimeWindow(0, 0, 25, 0))
        self.assertEqual(result.phobos, TimeWindow(0, 0, 5, 0))


class TestTimeWindowNormalizer(unittest.TestCase):
    """Test Component B: TimeWindowNormalizer"""

    def setUp(self):
        self.normalizer = TimeWindowNormalizer()

    def test_normalize_simple_interval(self):
        """Test normalization of non-wraparound interval."""
        windows = ParsedWindows(
            deimos=TimeWindow(5, 0, 10, 0),
            phobos=TimeWindow(8, 0, 12, 0),
        )
        result = self.normalizer.normalize(windows)
        self.assertEqual(result.deimos_intervals, [(500, 1000)])
        self.assertEqual(result.phobos_intervals, [(800, 1200)])

    def test_normalize_wraparound_interval(self):
        """Test normalization of midnight-wraparound interval."""
        windows = ParsedWindows(
            deimos=TimeWindow(24, 53, 7, 12),
            phobos=TimeWindow(5, 12, 8, 45),
        )
        result = self.normalizer.normalize(windows)
        # 24:53 = 2453, 7:12 = 712, so wraparound: [(2453, 2500), (0, 712)]
        self.assertEqual(result.deimos_intervals, [(2453, 2500), (0, 712)])
        # 5:12 = 512, 8:45 = 845, simple interval
        self.assertEqual(result.phobos_intervals, [(512, 845)])

    def test_normalize_full_day_interval(self):
        """Test normalization when start == end (full sol visibility)."""
        windows = ParsedWindows(
            deimos=TimeWindow(10, 0, 10, 0),
            phobos=TimeWindow(5, 0, 6, 0),
        )
        result = self.normalizer.normalize(windows)
        self.assertEqual(result.deimos_intervals, [(0, MARS_MINUTES_PER_DAY)])

    def test_normalize_25_00_wraps_to_midnight_no_zero_length_interval(self):
        """Test that 25:00 correctly wraps to midnight WITHOUT zero-length artifact.

        CRITICAL FIX: [10:00, 25:00] should normalize to [(1000, 2500)] only,
        NOT [(1000, 2500), (0, 0)]. This satisfies the invariant that all
        intervals have positive length (start < end).
        """
        windows = ParsedWindows(
            deimos=TimeWindow(10, 0, 25, 0),
            phobos=TimeWindow(0, 0, 5, 0),
        )
        result = self.normalizer.normalize(windows)
        # 10:00 = 1000, 25:00 % 2500 = 0
        # Since start (1000) > end (0), it's wraparound
        # NEW: Only [(1000, 2500)] because second interval would be zero-length
        self.assertEqual(result.deimos_intervals, [(1000, 2500)])


class TestOverlapCalculator(unittest.TestCase):
    """Test Component C: OverlapCalculator"""

    def setUp(self):
        self.calculator = OverlapCalculator()

    def test_calculate_full_overlap(self):
        """Test overlap calculation for identical intervals."""
        windows = NormalizedWindows(
            deimos_intervals=[(500, 1000)],
            phobos_intervals=[(500, 1000)],
        )
        result = self.calculator.calculate(windows)
        self.assertEqual(result.minutes, 500)

    def test_calculate_partial_overlap(self):
        """Test overlap calculation for partially overlapping intervals."""
        windows = NormalizedWindows(
            deimos_intervals=[(500, 1000)],
            phobos_intervals=[(800, 1200)],
        )
        result = self.calculator.calculate(windows)
        self.assertEqual(result.minutes, 200)  # 800 to 1000

    def test_calculate_no_overlap(self):
        """Test overlap calculation for non-overlapping intervals."""
        windows = NormalizedWindows(
            deimos_intervals=[(500, 1000)],
            phobos_intervals=[(1200, 1500)],
        )
        result = self.calculator.calculate(windows)
        self.assertEqual(result.minutes, 0)

    def test_calculate_wraparound_overlap(self):
        """Test overlap with wraparound intervals."""
        windows = NormalizedWindows(
            deimos_intervals=[(2453, 2500), (0, 712)],
            phobos_intervals=[(512, 845)],
        )
        result = self.calculator.calculate(windows)
        # Overlap: (512, 712) = 200 minutes
        self.assertEqual(result.minutes, 200)

    def test_calculate_adjacent_intervals_no_overlap(self):
        """Test that adjacent intervals (touching at boundary) have 0 overlap."""
        windows = NormalizedWindows(
            deimos_intervals=[(500, 1000)],
            phobos_intervals=[(1000, 1500)],
        )
        result = self.calculator.calculate(windows)
        self.assertEqual(result.minutes, 0)


class TestDurationExtractor(unittest.TestCase):
    """Test Component D: DurationExtractor (Twilight Rule)"""

    def setUp(self):
        self.extractor = DurationExtractor()

    def test_extract_nonzero_overlap(self):
        """Test that non-zero overlap is returned unchanged."""
        overlap = OverlapResult(minutes=200)
        windows = NormalizedWindows(
            deimos_intervals=[(500, 1000)],
            phobos_intervals=[(500, 1000)],
        )
        result = self.extractor.extract(overlap, windows)
        self.assertEqual(result, 200)

    def test_extract_twilight_rule_applies(self):
        """Test Twilight Rule: shared boundary point returns 1."""
        overlap = OverlapResult(minutes=0)
        windows = NormalizedWindows(
            deimos_intervals=[(500, 1000)],
            phobos_intervals=[(1000, 1500)],
        )
        result = self.extractor.extract(overlap, windows)
        self.assertEqual(result, 1)  # Shared boundary at 1000

    def test_extract_no_overlap_no_twilight(self):
        """Test no overlap and no shared boundary returns 0."""
        overlap = OverlapResult(minutes=0)
        windows = NormalizedWindows(
            deimos_intervals=[(500, 1000)],
            phobos_intervals=[(1500, 2000)],
        )
        result = self.extractor.extract(overlap, windows)
        self.assertEqual(result, 0)

    def test_extract_midnight_boundary_twilight(self):
        """Test Twilight Rule with midnight boundary (0 ≡ 2500)."""
        overlap = OverlapResult(minutes=0)
        windows = NormalizedWindows(
            deimos_intervals=[(1000, 2500)],  # Ends at midnight (2500)
            phobos_intervals=[(0, 500)],  # Starts at midnight (0)
        )
        result = self.extractor.extract(overlap, windows)
        # 2500 % 2500 = 0, and phobos has 0, so they share boundary point
        self.assertEqual(result, 1)


class TestMoonFunction(unittest.TestCase):
    """Test the integrated moon() function (all components together)"""

    def test_moon_example_1_partial_overlap(self):
        """Test REQ2 example 1: 100 minutes overlap."""
        # D[13:91, 23:05] P[22:05, 24:45]
        # D: 1391 to 2305, P: 2205 to 2445
        # Overlap: 2205 to 2305 = 100 minutes
        result = moon(13, 91, 23, 5, 22, 5, 24, 45)
        self.assertEqual(result, 100)

    def test_moon_example_2_wraparound(self):
        """Test REQ2 example 2: 200 minutes with wraparound."""
        # D[24:53, 7:12], P[5:12, 8:45]
        # D: [(2453, 2500), (0, 712)], P: [(512, 845)]
        # Overlap: 512 to 712 = 200 minutes
        result = moon(24, 53, 7, 12, 5, 12, 8, 45)
        self.assertEqual(result, 200)

    def test_moon_example_3_twilight_rule(self):
        """Test REQ3 example 1: Twilight rule with shared boundary."""
        # D[12:32, 17:06], P[17:06, 19:78]
        # D: 1232 to 1706, P: 1706 to 1978
        # No overlap, but shared boundary at 1706 -> 1 minute
        result = moon(12, 32, 17, 6, 17, 6, 19, 78)
        self.assertEqual(result, 1)

    def test_moon_example_4_no_overlap(self):
        """Test no overlap case."""
        # D[5:00, 6:00], P[7:00, 8:00]
        # D: 500 to 600, P: 700 to 800
        # No overlap, no shared boundary -> 0
        result = moon(5, 0, 6, 0, 7, 0, 8, 0)
        self.assertEqual(result, 0)

    def test_moon_example_5_midnight_twilight(self):
        """Test REQ3 midnight boundary: D[10:00, 25:00], P[0:00, 5:00]."""
        # D: 1000 to 0 (wraparound), P: 0 to 500
        # D normalizes to [(1000, 2500), (0, 0)]
        # No geometric overlap, but 2500 % 2500 = 0 matches P's start
        result = moon(10, 0, 25, 0, 0, 0, 5, 0)
        self.assertEqual(result, 1)

    def test_moon_full_day_visibility(self):
        """Test when one moon is visible all day."""
        # D visible all day: [5:00, 5:00]
        # P visible partially: [10:00, 15:00]
        # Overlap should be P's duration: 500 minutes
        result = moon(5, 0, 5, 0, 10, 0, 15, 0)
        self.assertEqual(result, 500)


if __name__ == "__main__":
    unittest.main(verbosity=2)

from __future__ import annotations

from pytest import mark, param

from leet_code.summary_ranges import summary_ranges


class TestSummaryRanges:
    @mark.parametrize(
        ("nums", "expected"),
        [
            param([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
            param([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ],
        ids=str,
    )
    def test_main(self, *, nums: list[int], expected: list[str]) -> None:
        assert summary_ranges(nums) == expected

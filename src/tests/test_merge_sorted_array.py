from __future__ import annotations

from pytest import mark, param

from leet_code.merge_sorted_array import merge_sorted_array


class TestMergeSortedArray:
    @mark.parametrize(
        ("nums1", "nums2", "expected"),
        [
            param([1, 2, 3, 0, 0, 0], [2, 5, 6], [1, 2, 2, 3, 5, 6]),
            param([2, 5, 6, 0, 0, 0], [1, 2, 3], [1, 2, 2, 3, 5, 6]),
            param([1], [], [1]),
            param([0], [1], [1]),
        ],
        ids=str,
    )
    def test_main(
        self, *, nums1: list[int], nums2: list[int], expected: list[int]
    ) -> None:
        m, n = len(nums1), len(nums2)
        merge_sorted_array(nums1, m, nums2, n)
        assert nums1 == expected

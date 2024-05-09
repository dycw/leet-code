from __future__ import annotations

from itertools import chain, repeat

from hypothesis import assume, given
from hypothesis.strategies import DataObject, data, integers
from pytest import mark, param
from utilities.hypothesis import lists_fixed_length

from leet_code.merge_sorted_array import merge_sorted_array


class TestMergeSortedArray:
    @mark.parametrize(
        ("nums1", "nums2", "expected"),
        [
            param([1, 2, 3, 0, 0, 0], [2, 5, 6], [1, 2, 2, 3, 5, 6]),
            param([2, 5, 6, 0, 0, 0], [1, 2, 3], [1, 2, 2, 3, 5, 6]),
            param([1], [], [1]),
            param([0], [1], [1]),
            param([4, 0, 0, 0, 0, 0], [1, 2, 3, 5, 6], [1, 2, 3, 4, 5, 6]),
        ],
        ids=str,
    )
    def test_main(
        self, *, nums1: list[int], nums2: list[int], expected: list[int]
    ) -> None:
        n = len(nums2)
        m = len(nums1) - n
        merge_sorted_array(nums1, m, nums2, n)
        assert nums1 == expected

    @given(data=data())
    def test_generic(self, *, data: DataObject) -> None:
        max_mn = 20  # problem is 200
        m = data.draw(integers(0, max_mn))
        n = data.draw(integers(0, max_mn))
        _ = assume(1 <= m + n <= max_mn)
        nums1_core = sorted(data.draw(lists_fixed_length(integers(-100, 100), m)))
        nums1 = list(chain(nums1_core, repeat(0, times=n)))
        nums2 = sorted(data.draw(lists_fixed_length(integers(-100, 100), n)))
        merge_sorted_array(nums1, m, nums2, n)
        expected = sorted(chain(nums1_core, nums2))
        assert nums1 == expected

    @given(data=data())
    def test_generic(self, *, data: DataObject) -> None:
        m = data.draw(integers(0, 200))
        n = data.draw(integers(0, 200))
        _ = assume(1 <= m + n <= 200)
        nums1_without_zeros = sorted(
            data.draw(lists_fixed_length(integers(-100, 100), m))
        )
        nums1 = list(chain(nums1_without_zeros, repeat(0, times=n)))
        nums2 = sorted(data.draw(lists_fixed_length(integers(-100, 100), n)))
        merge_sorted_array(nums1, m, nums2, n)
        expected = sorted(chain(nums1_without_zeros, nums2))
        assert nums1 == expected

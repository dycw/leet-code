from __future__ import annotations

from hypothesis import given
from hypothesis.strategies import DataObject, data, integers, lists
from pytest import mark, param

from leet_code.remove_element import remove_element


class TestRemoveElement:
    @mark.parametrize(
        ("nums", "val", "expected"),
        [
            param([3, 2, 2, 3], 3, [2, 2]),
            param([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3]),
        ],
        ids=str,
    )
    def test_main(self, *, nums: list[int], val: int, expected: list[int]) -> None:
        remove_element(nums, val)
        assert sorted(nums) == sorted(expected)

    @given(data=data())
    def test_generic(self, *, data: DataObject) -> None:
        nums = data.draw(lists(integers(0, 50), min_size=0, max_size=100))
        val = data.draw(integers(0, 100))
        remove_element(nums, val)
        non_val = [v for v in nums if v != val]
        assert sorted(nums) == sorted(non_val)

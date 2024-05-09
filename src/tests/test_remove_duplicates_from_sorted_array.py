from __future__ import annotations

from pytest import mark, param

from leet_code.remove_duplicates_from_sorted_array import remove_duplicates


class TestRemoveDuplicates:
    @mark.parametrize(
        ("nums", "expected_array", "expected_k"),
        [
            param([1, 1, 2], [1, 2], 2),
            param([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
        ],
        ids=str,
    )
    def test_main(
        self, *, nums: list[int], expected_array: list[int], expected_k: int
    ) -> None:
        assert remove_duplicates(nums) == expected_k
        assert nums[:expected_k] == expected_array

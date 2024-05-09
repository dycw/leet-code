from __future__ import annotations

from pytest import mark, param

from leet_code.average_of_levels_in_binary_tree import average_of_levels
from leet_code.structures import TreeNode


class TestAverageOfLevels:
    @mark.parametrize(
        ("root", "expected"),
        [
            param(TreeNode.from_list([3, 9, 20, None, None, 15, 7]), [3.0, 14.5, 11.0]),
            param(TreeNode.from_list([3, 9, 20, 15, 7, None, None]), [3.0, 14.5, 11.0]),
        ],
        ids=str,
    )
    def test_main(self, *, root: TreeNode | None, expected: list[float]) -> None:
        assert average_of_levels(root=root) == expected

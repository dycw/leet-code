from __future__ import annotations

from pytest import mark, param

from leet_code.maximum_depth_of_binary_tree import max_depth
from leet_code.structures import TreeNode


class TestMaxDepth:
    @mark.parametrize(
        ("root", "expected"),
        [
            param(TreeNode.from_list([3, 9, 20, None, None, 15, 7]), 3),
            param(TreeNode.from_list([1, None, 2]), 2),
        ],
        ids=str,
    )
    def test_main(self, *, root: TreeNode | None, expected: int) -> None:
        assert max_depth(root=root) == expected

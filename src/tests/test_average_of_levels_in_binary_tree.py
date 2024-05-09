from __future__ import annotations

from pytest import mark, param

from leet_code.average_of_levels_in_binary_tree import average_of_levels
from leet_code.structures import TreeNode

case_1_node_0 = TreeNode(val=3)
case_1_node_1 = TreeNode(val=9)
case_1_node_2 = TreeNode(val=20)
case_1_node_3 = TreeNode(val=15)
case_1_node_4 = TreeNode(val=7)
case_1_node_0.left = case_1_node_1
case_1_node_0.right = case_1_node_2
case_1_node_2.left = case_1_node_3
case_1_node_2.right = case_1_node_4


case_2_node_0 = TreeNode(val=3)
case_2_node_1 = TreeNode(val=9)
case_2_node_2 = TreeNode(val=20)
case_2_node_3 = TreeNode(val=15)
case_2_node_4 = TreeNode(val=7)
case_2_node_0.left = case_2_node_1
case_2_node_0.right = case_2_node_2
case_2_node_1.left = case_2_node_3
case_2_node_1.right = case_2_node_4


class TestMaxDepth:
    @mark.parametrize(
        ("root", "expected"),
        [
            param(case_1_node_0, [3.0, 14.5, 11.0]),
            param(case_2_node_0, [3.0, 14.5, 11.0]),
        ],
        ids=str,
    )
    def test_main(self, *, root: TreeNode | None, expected: list[float]) -> None:
        assert average_of_levels(root=root) == expected

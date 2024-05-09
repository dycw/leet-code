from __future__ import annotations

from pytest import mark, param

from leet_code.maximum_depth_of_binary_tree import TreeNode, max_depth

case_1_node_0 = TreeNode(val=3)
case_1_node_1 = TreeNode(val=9)
case_1_node_2 = TreeNode(val=20)
case_1_node_3 = TreeNode(val=15)
case_1_node_4 = TreeNode(val=7)
case_1_node_0.left = case_1_node_1
case_1_node_0.right = case_1_node_2
case_1_node_2.left = case_1_node_3
case_1_node_2.right = case_1_node_4


case_2_node_0 = TreeNode(val=1)
case_2_node_1 = TreeNode(val=2)
case_2_node_0.right = case_2_node_1


class TestMaxDepth:
    @mark.parametrize(
        ("root", "expected"),
        [param(case_1_node_0, 3), param(case_2_node_0, 2)],
        ids=str,
    )
    def test_main(self, *, root: TreeNode | None, expected: int) -> None:
        assert max_depth(root=root) == expected

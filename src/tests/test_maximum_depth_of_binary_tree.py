from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.maximum_depth_of_binary_tree import TreeNode, max_depth

if TYPE_CHECKING:
    from leet_code.linked_list_cycle import ListNode

case_1_node_0 = TreeNode(3)
case_1_node_1 = TreeNode(9)
case_1_node_2 = TreeNode(20)
case_1_node_3 = TreeNode(15)
case_1_node_4 = TreeNode(7)
case_1_node_0.left = case_1_node_1
case_1_node_0.right = case_1_node_2
case_1_node_2.left = case_1_node_3
case_1_node_2.right = case_1_node_4


case_2_node_0 = TreeNode(1)
case_2_node_1 = TreeNode(2)
case_2_node_0.right = case_2_node_1


class TestMaxDepth:
    @mark.parametrize(
        ("root", "expected"),
        [param(case_1_node_0, 3), param(case_2_node_0, 2)],
        ids=str,
    )
    def test_main(self, *, root: ListNode | None, expected: int) -> None:
        assert max_depth(root=root) == expected

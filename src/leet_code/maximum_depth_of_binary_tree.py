"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        *,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        super().__init__()
        self.val = val
        self.left = left
        self.right = right


def max_depth(*, root: TreeNode | None = None) -> int:
    if root is None:
        return 0
    left_depth = max_depth(root=root.left) + 1
    right_depth = max_depth(root=root.right) + 1
    return max(left_depth, right_depth)

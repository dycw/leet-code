"""
530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105


Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""

from __future__ import annotations

from contextlib import suppress
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from leet_code.structures import TreeNode


def get_minimum_difference(*, root: TreeNode | None = None) -> int:
    if root is None:
        return 0
    candidates: list[int] = []
    if (left := root.left) is not None:
        candidates.append(abs(root.val - left.val))
        with suppress(ValueError):
            candidates.append(get_minimum_difference(root=left))
    if (right := root.right) is not None:
        candidates.append(abs(root.val - right.val))
        with suppress(ValueError):
            candidates.append(get_minimum_difference(root=right))
    return min(candidates)

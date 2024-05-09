"""
637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

    from leet_code.structures import TreeNode


def average_of_levels(*, root: TreeNode | None = None) -> list[float]:
    if root is None:
        return []
    return list(yield_averages_by_level(root))


def yield_averages_by_level(root: TreeNode, /) -> Iterator[float]:
    nodes = [root]
    while (length := len(nodes)) >= 1:
        yield sum(node.val for node in nodes) / length
        nodes = list(yield_children(nodes))


def yield_children(nodes: Iterable[TreeNode], /) -> Iterator[TreeNode]:
    for node in nodes:
        if (left := node.left) is not None:
            yield left
        if (right := node.right) is not None:
            yield right

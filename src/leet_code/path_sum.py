"""
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

    from leet_code.structures import TreeNode


def has_path_sum(target_sum: int, /, *, root: TreeNode | None = None) -> bool:
    if root is None:
        return False
    return any(_path_sum(path) == target_sum for path in _yield_paths(root))


def _yield_paths(
    node: TreeNode, /, *, head: Iterable[TreeNode] | None = None
) -> Iterator[Iterable[TreeNode]]:
    left, right = node.left, node.right
    init_head = [] if head is None else head
    new_head = list(chain(init_head, [node]))
    if (left is None) and (right is None):  # leaf
        yield new_head
    else:
        if left is not None:
            yield from _yield_paths(left, head=new_head)
        if right is not None:
            yield from _yield_paths(right, head=new_head)


def _path_sum(nodes: Iterable[TreeNode], /) -> int:
    return sum(node.val for node in nodes)


def has_path_sum_top(target_sum: int, /, *, root: TreeNode | None = None) -> bool:
    if not root:
        return False
    if root.val == target_sum and not root.left and not root.right:
        return True
    return has_path_sum_top(target_sum - root.val, root=root.left) or has_path_sum_top(
        target_sum - root.val, root=root.right
    )

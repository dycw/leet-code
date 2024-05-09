from __future__ import annotations

from itertools import accumulate, chain, pairwise, repeat
from math import log2
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from collections.abc import Iterable


class ListNode:
    def __init__(self, x: int, /) -> None:
        super().__init__()
        self.val = x
        self.next: ListNode | None = None

    @override
    def __repr__(self) -> str:
        parts = [f"val={self.val}"]
        if (next_ := self.next) is not None:
            parts.append(f"next={next_}")
        joined = ", ".join(parts)
        return f"{type(self).__name__}({joined})"


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

    @classmethod
    def from_list(cls, values: Iterable[int | None], /) -> TreeNode:
        values = list(values)
        num_levels = cls.get_num_of_levels(len(values))
        lengths_by_level = [2**i for i in range(num_levels)]
        nodes: list[list[TreeNode | None]] = [
            list(repeat(None, times=length)) for length in lengths_by_level
        ]
        endpoints = list(chain([0], accumulate(lengths_by_level)))
        for i, (start, end) in zip(range(num_levels), pairwise(endpoints), strict=True):
            values_i = values[start:end]
            nodes[i][:] = [None if v is None else TreeNode(val=v) for v in values_i]
        for i in range(num_levels - 1):
            nodes_i1 = nodes[i + 1]
            for j, node_j in enumerate(nodes[i]):
                if node_j is not None:
                    node_j.left = nodes_i1[2 * j]
                    node_j.right = nodes_i1[2 * j + 1]
        (root,) = nodes[0]
        if root is not None:
            return root
        msg = "The root must not be None"
        raise TypeError(msg)

    @staticmethod
    def get_num_of_levels(num_nodes: int, /) -> int:
        levels = log2(num_nodes + 1)
        if levels == round(levels):
            return int(levels)
        msg = f"{num_nodes} is not a valid number of nodes"
        raise ValueError(msg)

    @override
    def __repr__(self) -> str:
        parts = [f"val={self.val}"]
        if (left := self.left) is not None:
            parts.append(f"left={left}")
        if (right := self.right) is not None:
            parts.append(f"right={right}")
        joined = ", ".join(parts)
        return f"{type(self).__name__}({joined})"

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

from __future__ import annotations

from typing import override


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

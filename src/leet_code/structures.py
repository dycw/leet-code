from __future__ import annotations


class ListNode:
    def __init__(self, x: int, /) -> None:
        super().__init__()
        self.val = x
        self.next: ListNode | None = None


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

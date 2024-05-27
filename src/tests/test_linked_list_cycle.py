from __future__ import annotations

from pytest import mark, param

from leet_code.linked_list_cycle import has_cycle
from leet_code.structures import ListNode

case_1_node_0 = ListNode(3)
case_1_node_1 = ListNode(2)
case_1_node_2 = ListNode(0)
case_1_node_3 = ListNode(-4)
case_1_node_0.next = case_1_node_1
case_1_node_1.next = case_1_node_2
case_1_node_2.next = case_1_node_3
case_1_node_3.next = case_1_node_1


case_2_node_0 = ListNode(1)
case_2_node_1 = ListNode(2)
case_2_node_0.next = case_2_node_1
case_2_node_1.next = case_2_node_0


case_3_node_0 = ListNode(1)


class TestHasCycle:
    @mark.parametrize(
        ("head", "expected"),
        [
            param(case_1_node_0, True),
            param(case_2_node_0, True),
            param(case_3_node_0, False),
        ],
    )
    def test_main(self, *, head: ListNode | None, expected: bool) -> None:
        assert has_cycle(head=head) is expected

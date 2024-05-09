from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.minimum_absolute_difference_in_bst import get_minimum_difference
from leet_code.structures import TreeNode

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture

case_1_node_0 = TreeNode(val=4)
case_1_node_1 = TreeNode(val=2)
case_1_node_2 = TreeNode(val=6)
case_1_node_3 = TreeNode(val=1)
case_1_node_4 = TreeNode(val=3)
case_1_node_0.left = case_1_node_1
case_1_node_0.right = case_1_node_2
case_1_node_1.left = case_1_node_3
case_1_node_1.right = case_1_node_4


case_2_node_0 = TreeNode(val=1)
case_2_node_1 = TreeNode(val=0)
case_2_node_2 = TreeNode(val=48)
case_2_node_3 = TreeNode(val=12)
case_2_node_4 = TreeNode(val=49)
case_2_node_0.left = case_2_node_1
case_2_node_0.right = case_2_node_2
case_2_node_2.left = case_2_node_3
case_2_node_2.right = case_2_node_4


class TestGetMinimumDifference:
    @mark.parametrize("func", [param(get_minimum_difference)])
    @mark.parametrize(
        ("root", "expected"),
        [
            param(case_1_node_0, 1, marks=mark.benchmark(group="1")),
            param(case_2_node_0, 1, marks=mark.benchmark(group="2")),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[[int], bool],
        root: TreeNode | None,
        expected: bool,
    ) -> None:
        assert benchmark(func, root=root) == expected

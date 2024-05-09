from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.path_sum import has_path_sum, has_path_sum_top
from leet_code.structures import TreeNode

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture

case_1_node_0 = TreeNode(val=5)
case_1_node_1 = TreeNode(val=4)
case_1_node_2 = TreeNode(val=8)
case_1_node_3 = TreeNode(val=11)
case_1_node_4 = TreeNode(val=13)
case_1_node_5 = TreeNode(val=4)
case_1_node_6 = TreeNode(val=7)
case_1_node_7 = TreeNode(val=2)
case_1_node_8 = TreeNode(val=1)
case_1_node_0.left = case_1_node_1
case_1_node_0.right = case_1_node_2
case_1_node_1.left = case_1_node_3
case_1_node_2.left = case_1_node_4
case_1_node_2.right = case_1_node_5
case_1_node_3.left = case_1_node_6
case_1_node_3.right = case_1_node_7
case_1_node_5.right = case_1_node_8


case_2_node_0 = TreeNode(val=1)
case_2_node_1 = TreeNode(val=2)
case_2_node_2 = TreeNode(val=3)
case_2_node_0.left = case_2_node_1
case_2_node_0.right = case_2_node_2


class TestPathSum:
    @mark.parametrize("func", [param(has_path_sum), param(has_path_sum_top)])
    @mark.parametrize(
        ("root", "target_sum", "expected"),
        [
            param(case_1_node_0, 22, True, marks=mark.benchmark(group="1")),
            param(case_2_node_0, 5, False, marks=mark.benchmark(group="2")),
            param(None, 0, False, marks=mark.benchmark(group="3")),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[[int], bool],
        root: TreeNode | None,
        target_sum: int,
        expected: bool,
    ) -> None:
        assert benchmark(func, target_sum, root=root) is expected

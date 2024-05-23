from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.path_sum import has_path_sum, has_path_sum_top
from leet_code.structures import TreeNode

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture


class TestPathSum:
    @mark.parametrize("func", [param(has_path_sum), param(has_path_sum_top)])
    @mark.parametrize(
        ("root", "target_sum", "expected"),
        [
            param(
                TreeNode.from_list(
                    [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
                ),
                22,
                True,
                marks=mark.benchmark(group="1"),
            ),
            param(
                TreeNode.from_list([1, 2, 3]), 5, False, marks=mark.benchmark(group="2")
            ),
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

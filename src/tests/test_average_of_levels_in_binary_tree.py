from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.average_of_levels_in_binary_tree import (
    average_of_levels,
    average_of_levels_top,
)
from leet_code.structures import TreeNode

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture


class TestAverageOfLevels:
    @mark.parametrize("func", [param(average_of_levels), param(average_of_levels_top)])
    @mark.parametrize(
        ("root", "expected"),
        [
            param(
                TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
                [3.0, 14.5, 11.0],
                marks=mark.benchmark(group="1"),
            ),
            param(
                TreeNode.from_list([3, 9, 20, 15, 7, None, None]),
                [3.0, 14.5, 11.0],
                marks=mark.benchmark(group="2"),
            ),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[..., list[float]],
        root: TreeNode | None,
        expected: list[float],
    ) -> None:
        assert benchmark(func, root=root) == expected

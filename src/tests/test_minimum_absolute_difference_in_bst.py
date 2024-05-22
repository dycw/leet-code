from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.minimum_absolute_difference_in_bst import get_minimum_difference

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture

from leet_code.structures import TreeNode


class TestGetMinimumDifference:
    @mark.parametrize("func", [param(get_minimum_difference)])
    @mark.parametrize(
        ("root", "expected"),
        [
            param(
                TreeNode.from_list([4, 2, 6, 1, 3, None, None]),
                1,
                marks=mark.benchmark(group="1"),
            ),
            param(
                TreeNode.from_list([1, 0, 48, None, None, 12, 49]),
                1,
                marks=mark.benchmark(group="2"),
            ),
            param(
                TreeNode.from_list([236, 104, 701, None, 227, None, 911]),
                9,
                marks=mark.benchmark(group="3"),
            ),
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

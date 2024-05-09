from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.plus_one import plus_one, plus_one_top

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture


class TestPlusOne:
    @mark.parametrize("func", [param(plus_one), param(plus_one_top)])
    @mark.parametrize(
        ("digits", "expected"),
        [
            param([1, 2, 3], [1, 2, 4], marks=mark.benchmark(group="1")),
            param([4, 3, 2, 1], [4, 3, 2, 2], marks=mark.benchmark(group="2")),
            param([9], [1, 0], marks=mark.benchmark(group="3")),
            param([8, 9, 9, 9], [9, 0, 0, 0], marks=mark.benchmark(group="4")),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[[list[int]], list[int]],
        digits: list[int],
        expected: list[int],
    ) -> None:
        assert benchmark(lambda: func(deepcopy(digits))) == expected

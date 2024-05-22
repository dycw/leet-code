from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.majority_element import majority_element, majority_element_top

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture


class TestMajorityElement:
    @mark.parametrize("func", [param(majority_element), param(majority_element_top)])
    @mark.parametrize(
        ("nums", "expected"),
        [
            param([3, 2, 3], 3, marks=mark.benchmark(group="1")),
            param([2, 2, 1, 1, 1, 2, 2], 2, marks=mark.benchmark(group="2")),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[[int], bool],
        nums: list[int],
        expected: bool,
    ) -> None:
        assert benchmark(func, nums) == expected

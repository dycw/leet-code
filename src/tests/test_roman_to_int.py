from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.roman_to_integer import roman_to_int, roman_to_int_top

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture


class TestRomanToInt:
    @mark.parametrize("func", [param(roman_to_int), param(roman_to_int_top)])
    @mark.parametrize(
        ("s", "expected"),
        [
            param("III", 3, marks=mark.benchmark(group="1")),
            param("LVIII", 58, marks=mark.benchmark(group="2")),
            param("MCMXCIV", 1994, marks=mark.benchmark(group="3")),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[[str], int],
        s: str,
        expected: int,
    ) -> None:
        assert benchmark(func, s) == expected

from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

from leet_code.length_of_last_word import length_of_last_word, length_of_last_word_top

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture


class TestLengthOfLastWord:
    @mark.parametrize(
        "func", [param(length_of_last_word), param(length_of_last_word_top)]
    )
    @mark.parametrize(
        ("s", "expected"),
        [
            param("Hello World", 5, marks=mark.benchmark(group="1")),
            param("   fly me   to   the moon  ", 4, marks=mark.benchmark(group="2")),
            param("luffy is still joyboy", 6, marks=mark.benchmark(group="3")),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[[int], bool],
        s: str,
        expected: int,
    ) -> None:
        assert benchmark(func, s) == expected

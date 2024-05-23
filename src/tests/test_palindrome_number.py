from __future__ import annotations

from typing import TYPE_CHECKING

from pytest import mark, param

if TYPE_CHECKING:
    from collections.abc import Callable

    from pytest_benchmark.fixture import BenchmarkFixture


from leet_code.palindrome_number import is_palindrome, is_palindrome_top


class TestIsPalindrome:
    @mark.parametrize("func", [param(is_palindrome), param(is_palindrome_top)])
    @mark.parametrize(
        ("x", "expected"),
        [
            param(121, True, marks=mark.benchmark(group="1")),
            param(-121, False, marks=mark.benchmark(group="2")),
            param(10, False, marks=mark.benchmark(group="3")),
        ],
        ids=str,
    )
    def test_main(
        self,
        *,
        benchmark: BenchmarkFixture,
        func: Callable[[int], bool],
        x: int,
        expected: bool,
    ) -> None:
        assert benchmark(func, x) is expected

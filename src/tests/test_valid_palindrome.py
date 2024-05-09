from __future__ import annotations

from hypothesis import given
from hypothesis.strategies import DataObject, data, integers
from pytest import mark, param
from utilities.hypothesis import text_ascii

from leet_code.valid_palindrome import is_palindrome, is_palindrome_slow


class TestValidPalindrome:
    @mark.parametrize(
        ("s", "expected"),
        [
            param("A man, a plan, a canal: Panama", True),
            param("race a car", False),
            param(" ", True),
            param("0P", False),
        ],
        ids=str,
    )
    def test_main(self, *, s: str, expected: bool) -> None:
        assert is_palindrome(s) is expected
        assert is_palindrome_slow(s) is expected

    @given(data=data())
    def test_generic(self, *, data: DataObject) -> None:
        length = data.draw(integers(1, int(2e3)))  # is 2e5
        s = "".join(data.draw(text_ascii(min_size=length, max_size=length)))
        assert is_palindrome(s) is is_palindrome_slow(s)

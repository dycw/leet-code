from __future__ import annotations

from pytest import mark, param

from leet_code.ransom_note import can_construct


class TestCanConstruct:
    @mark.parametrize(
        ("ransom_note", "magazine", "expected"),
        [param("a", "b", False), param("aa", "a", False), param("aa", "aab", True)],
        ids=str,
    )
    def test_main(self, *, ransom_note: str, magazine: str, expected: bool) -> None:
        assert can_construct(ransom_note, magazine) is expected

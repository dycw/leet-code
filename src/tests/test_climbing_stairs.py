from __future__ import annotations

from pytest import mark, param

from leet_code.climbing_stairs import climb_stairs


class TestClimbStairs:
    @mark.parametrize(("n", "expected"), [param(2, 2), param(3, 3), param(4, 5)])
    def test_main(self, *, n: int, expected: int) -> None:
        assert climb_stairs(n) == expected

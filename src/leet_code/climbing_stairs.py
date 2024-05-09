"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

from __future__ import annotations

_CACHE: dict[int, int] = {}


def climb_stairs(n: int, /) -> int:
    if n <= 2:
        return n
    try:
        res_n2 = _CACHE[n - 2]
    except KeyError:
        res_n2 = _CACHE[n - 2] = climb_stairs(n - 2)
    try:
        res_n1 = _CACHE[n - 1]
    except KeyError:
        res_n1 = _CACHE[n - 1] = climb_stairs(n - 1)
    return res_n2 + res_n1

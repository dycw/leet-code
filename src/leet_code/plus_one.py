"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

from __future__ import annotations

from itertools import chain, repeat, takewhile


def plus_one(digits: list[int], /) -> list[int]:
    num_digits = len(digits)
    rev = reversed(digits)
    segment = list(takewhile(lambda d: d == 9, rev))
    num_nines = len(segment)
    if num_nines == 0:
        return list(chain(digits[:-1], [digits[-1] + 1]))
    if num_nines < num_digits:
        num_head = num_digits - num_nines
        return list(
            chain(
                digits[: num_head - 1],
                [digits[num_head - 1] + 1],
                repeat(0, times=num_nines),
            )
        )
    return list(chain([1], repeat(0, times=num_digits)))


def plus_one_top(digits: list[int], /) -> list[int]:
    for i, d in reversed(list(enumerate(digits))):
        if d < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1, *digits]

"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

from __future__ import annotations

from typing import Literal


def roman_to_int(s: str, /) -> int:
    total = 0
    i, n = 0, len(s)
    while i < n:
        if i < n - 1:
            try:
                value, inc = convert_double(s[i : i + 2])
            except KeyError:
                value, inc = convert_single(s[i])
        else:
            value, inc = convert_single(s[i])
        total += value
        i += inc
    return total


_SINGULAR_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def convert_single(s: str, /) -> tuple[int, Literal[1]]:
    return _SINGULAR_VALUES[s], 1


_DOUBLE_VALUES = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}


def convert_double(s: str, /) -> tuple[int, Literal[2]]:
    return _DOUBLE_VALUES[s], 2


def roman_to_int_top(s: str, /) -> int:
    roman_symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_ = 0
    prev_self = 0

    for s_i in reversed(s):
        if prev_self > roman_symbol[s_i]:
            sum_ -= roman_symbol[s_i]
        else:
            sum_ += roman_symbol[s_i]
            prev_self = roman_symbol[s_i]
    return sum_

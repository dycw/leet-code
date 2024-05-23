"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1


Follow up: Could you solve it without converting the integer to a string?
"""

from __future__ import annotations


def is_palindrome(x: int, /) -> bool:
    if x < 0:
        return False
    as_str = str(x)
    n_total = len(as_str)
    n_check = n_total // 2
    return as_str[:n_check] == as_str[: -(n_check + 1) : -1]


def is_palindrome_top(x: int, /) -> bool:
    str_x = str(x)
    return str_x == str_x[::-1]

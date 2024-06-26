"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

from __future__ import annotations

from itertools import dropwhile, takewhile


def length_of_last_word(s: str, /) -> int:
    return len(list(takewhile(str.isalpha, dropwhile(_is_space, s[::-1]))))


def _is_space(s: str, /) -> bool:
    return s == " "


def length_of_last_word_top(s: str, /) -> int:
    r = len(s) - 1
    count = 0
    while s[r] == " " and r >= 0:
        r -= 1
    while s[r] != " " and r >= 0:
        count += 1
        r -= 1
    return count

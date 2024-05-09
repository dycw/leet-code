"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

from __future__ import annotations


def is_palindrome(s: str, /) -> bool:
    letters = [c for c in s.lower() if c.isalnum()]
    n = len(letters)
    half = n // 2
    half_rev = (half - 1) if n % 2 == 0 else half
    return letters[:half] == letters[n - 1 : half_rev : -1]


def is_palindrome_slow(s: str, /) -> bool:
    letters = [c for c in s.lower() if c.isalnum()]
    return letters == letters[::-1]

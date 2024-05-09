"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

from __future__ import annotations

from collections import Counter  # faster than typing!


def can_construct(ransom_note: str, magazine: str, /) -> bool:
    ransom_note_counts = Counter(ransom_note)
    return all(
        _can_construct_key(letter, count, magazine)
        for letter, count in ransom_note_counts.items()
    )


def _can_construct_key(letter: str, count: int, magazine: str, /) -> bool:
    return count <= magazine.count(letter)

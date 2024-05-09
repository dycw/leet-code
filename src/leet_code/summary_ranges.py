"""
228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""

from __future__ import annotations

from itertools import count, starmap, takewhile
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator


def summary_ranges(nums: list[int], /) -> list[str]:
    return list(starmap(format_range, yield_ranges(nums)))


def yield_ranges(nums: list[int]) -> Iterator[tuple[int, int]]:
    i = 0
    while i < len(nums):
        value = nums[i]
        segment2 = takewhile(
            lambda x: x[0] == x[1], zip(nums[i:], count(start=value), strict=False)
        )
        segment1 = [x for x, _ in segment2]
        yield value, segment1[-1]
        i += len(segment1)


def format_range(start: int, end: int, /) -> str:
    return str(start) if start == end else f"{start}->{end}"

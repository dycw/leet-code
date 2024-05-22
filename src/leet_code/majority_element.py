"""
169. Majority Elemen

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from __future__ import annotations

from collections import defaultdict
from math import floor


def majority_element(nums: list[int]) -> int:
    n = len(nums)
    threshold = floor(n / 2)
    counts: defaultdict[int, int] = defaultdict(int)
    for num in nums:
        counts[num] += 1
        if counts[num] > threshold:
            return num
    raise ValueError


def majority_element_top(nums: list[int]) -> int:
    n = len(nums)
    return sorted(nums)[n // 2]

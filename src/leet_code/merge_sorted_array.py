"""
88. Merge Sorted arrays

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""

from __future__ import annotations

from rich import print

# init [<1>, 2, 3, 0, 0, 0], [<2>, 5, 6]
# since l < r, move left: [1, <2>, 3, 0, 0, 0], [<2>, 5, 6]
# since l >= r, insert: [1, 2, <2>, 3, 0, 0], [<5>, 6]
# since l < r, move left: [1, 2, 2, <3>, 0, 0], [<5>, 6]
# since l < r, terminate: [1, 2, 2, 3, <5, 6>], []

# init [<2>, 5, 6, 0, 0, 0], [<1>, 2, 3]
# since l >= r, insert: [1, <2>, 5, 6, 0, 0], [<2>, 3]
# since l >= r, insert: [1, 2, <2>, 5, 6, 0], [<3>]
# since l < r, move left: [1, 2, 2, <5>, 6, 0], [<3>]
# since l >= r, insert: [1, 2, 2, 3, <5>, 6], []


def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    index1, index2, num_left_checked, num_insertions = 0, 0, 0, 0
    max_left_check = m - n
    while (num_insertions < n) and (num_left_checked <= max_left_check):
        value1, value2 = nums1[index1], nums2[index2]
        print("loop start", locals())
        if value1 < value2:
            index1 += 1
            num_left_checked += 1
            print("after <", locals())
        else:
            nums1.insert(index1, value2)
            _ = nums1.pop()
            num_insertions += 1
            index1 += 1
            index2 += 1
            num_left_checked += 1
            print("after >=", locals())

    len_tail = n - num_insertions
    if len_tail >= 1:
        nums1[-len_tail:] = nums2[-len_tail:]

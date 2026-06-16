"""
input: integer array nums (len? empty? values? negatives?)
output: integer; represents largest sum from a subarray

brute force: for each possible subarray, find sum and return greatest; O(2^n)

optimal: two pointers which start at either end of array, bring the pointer with smaller value inward and update max sum

[2, -3, 4, -2, 2, 1, -1, 4] = 7, max = 7
[-3, 4, -2, 2, 1, -1, 4] = 5, max = 7
[4, -2, 2, 1, -1, 4] = 8, max = 8
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = 0

        for num in nums:
            if current < 0:
                current = 0
            current += num
            result = max(result, current)
        return result
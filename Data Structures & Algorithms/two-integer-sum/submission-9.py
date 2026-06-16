"""
input: integer array nums (empty? negatives? always valid solution), integer target (negative, possible?)
output: integer array that contains the indices of the values from the input array that add up to the target

1. for each value, iterate through the rest of the array until target is found and return. r: O(N^2) s:O(1)
2. for each value, store the difference from the target and for each future value, check if the difference already exists from map r: O(n) s: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i, num in enumerate(nums):
            remainder[target - num] = i

        for i, num in enumerate(nums):
            if num in remainder:
                second = remainder[num]
                if i != second:
                    return [min(i, second), max(i, second)]
        return
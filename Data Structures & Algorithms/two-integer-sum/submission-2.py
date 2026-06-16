"""
input: array int nums, int target
output: array int with 2 indices such that their respective values sum to target
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in hashmap):
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i
        return
"""
inputs: nums = int array; target = int;
output: index i, index j = location of two ints that add up to target
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digits = {}
        for i in range(len(nums)):  
            if target - nums[i] in digits:  
                return [digits[target - nums[i]], i]  
            digits[nums[i]] = i  


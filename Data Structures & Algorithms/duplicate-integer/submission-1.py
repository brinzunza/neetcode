"""
input: int array nums
output: boolean, true if value appears more than once, false otherwise

make a set, if set is smaller than nums, then true, else then false
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(set(nums)) < len(nums)):
            return True
        else:
            return False
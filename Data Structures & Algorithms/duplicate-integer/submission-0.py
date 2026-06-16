"""
inputs: nums = int array
output: boolean = true if any value appears more than once, else false

can nums be empty?
what values can be in nums?
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueValues = set(nums)
        if(len(uniqueValues) == len(nums)):
            return False;
        else:
            return True;
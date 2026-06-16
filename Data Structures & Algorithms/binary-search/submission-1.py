"""
Input: int array nums, int target
output: int, index of target in nums

len nums? 0?
always valid target?

keep a pointer at half way of curr array, if value is larger then cut lower half out, else cut higher half out. Move pointer to new halfway and repeat until value is found. 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        half = end // 2
        while(start <= end):
            if(nums[half] == target):
                return half
            elif(target > nums[half]):
                start = half + 1
                half = (end + start) // 2
            else:
                end = half - 1
                half = (end + start) // 2
        return -1
"""
input: int array nums
output: int, min element of array

binary search 
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        smallest = nums[0]
        while(start <= end):
            half = (start + end) // 2
            if(nums[half] < smallest):
                smallest = nums[half]
            if(nums[half] > nums[end]):
                start = half + 1
            else:
                end = half - 1
        return smallest

"""
Time complexity: O(logn)
Space complexity: O(1)
"""
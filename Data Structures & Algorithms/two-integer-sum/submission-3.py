"""
input: array integers nums, integer target
output: array of ints, indices of both integers

iterate through array, checking if complementary num is in map, if so, return indices, else add value to map
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if(comp in map):
                return [map[comp], i]
            else:
                map[nums[i]] = i
        return []

"""
Time complexity: O(n)
Space Complexity: O(n)
"""
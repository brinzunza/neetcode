"""
input: int array nums
output: boolean, true if duplicates exist, false otherwise

size of array? empty?

keep map to track if int has appeared, constantly check for each if already in map. Return true if so, false otherwise
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if i in map:
                return True
            else:
                map[i] = None
        return False

"""
Time complexity: O(n)
Space complexity: O(n)
"""
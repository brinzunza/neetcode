"""
input: integer array nums (empty? size? null values? negatives?)
output: return true if any values appears more than once, false otherwise

1. keep map of set of values seen, if any exist in map, return true; r: O(n) s: O(n)

2. for each value, iterate through the rest of the array and check if same value exists; r: O(N^2) s: O(1)

3. sort array and check adjacent values; r: O(nlogn) O(1)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = 0

        return False
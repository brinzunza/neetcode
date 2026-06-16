"""
O(N)
O(N)


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        #fills up hashmap with differences (target - nums)
        for i, num in enumerate(nums):
            differences[target - num] = i

        #iterating through nums and find solution 
        for i, num in enumerate(nums):
            retrieved = differences.get(num, -1)
            if retrieved != -1 and retrieved != i:
                return [min(retrieved, i), max(retrieved, i)]

        return
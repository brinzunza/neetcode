class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        for i, num in enumerate(nums):
            rem = target - num
            if num in remainders:
                return [remainders[num], i]
            else:
                remainders[rem] = i

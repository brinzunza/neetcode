class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in remainder:
                return [remainder[rem], i]
            remainder[nums[i]] = i

        return []
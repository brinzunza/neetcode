class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missing = nums[0]
        for num in nums[1:]:
            missing = missing ^ num

        return missing
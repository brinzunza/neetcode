"""
input: int array nums
output: int array

with 1 zero
with more than 1 zero
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if(len(nums) < 2):
            return nums
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
        if(zeros > 1):
            return [0 for _ in range(len(nums))]

        product = 1
        for i in nums:
            if(i != 0):
                product *= i

        result = []
        for i in nums:
            if(zeros == 1):
                if(i == 0):
                   result.append(product) 
                else:
                    result.append(0)
            else:
                result.append(int(product / i))

        return result
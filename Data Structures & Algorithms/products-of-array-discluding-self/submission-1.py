"""
input: nums = array of ints
output: output = array of ints

how large can nums[i] be
how many elements in nums
can nums be len 0 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                zeros += 1
        
        if zeros > 1:
            return [0] * len(nums)

        result = []
        for i in nums:
            if zeros == 0:
                result.append(int(product / i))
            elif i == 0:
                result.append(product)
            else:
                result.append(0)

        return result
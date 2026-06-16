"""
input: int array nums
output: int array, all solutions of three indices that add up to 0 and are all distinct. in any order

len of array? 0?
impossible solution?

 
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                added = nums[i] + nums[start] + nums[end]
                if added == 0:
                    results.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif added < 0:
                    start += 1
                else:
                    end -= 1

        return results
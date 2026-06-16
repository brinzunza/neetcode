"""
input: int array nums, int target
output: int, index of target value


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            half = (start + end) // 2

            if nums[half] == target:
                return half

            if nums[start] <= nums[half]:
                if nums[start] <= target < nums[half]:
                    end = half - 1
                else:
                    start = half + 1
            else:
                if nums[half] < target <= nums[end]:
                    start = half + 1
                else:
                    end = half - 1

        return -1

"""
Time complexity: O(log n)
Space complexity: O(1)
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(start, currentSum, currentNums):
            if(currentSum == target):
                result.append(currentNums[:])

            for i in range(start, len(nums)):
                if(currentSum + nums[i] <= target):
                    currentNums.append(nums[i])
                    backtracking(i, currentSum + nums[i], currentNums)
                    currentNums.pop()

        backtracking(0, 0, [])
        return result
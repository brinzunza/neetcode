"""
input: integer array nums(empty? negatives? always valid solution?)
output: 2d integer array; represents all the possible combinations
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        state = []

        def backtracking(i, state):
            result.append(state[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                state.append(nums[j])
                backtracking(j + 1, state)
                state.pop()

        backtracking(0, state)
        return result

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(position, state):
            result.append(state[:])
            for i in range(position, len(nums)):
                state.append(nums[i])
                backtracking(i + 1, state)
                state.pop()

        backtracking(0, [])
        return result
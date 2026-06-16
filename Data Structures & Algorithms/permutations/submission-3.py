class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(state):
            if len(state) == len(nums):
                result.append(state[:])
                return

            for num in nums:
                if num in state:
                    continue
                state.append(num)
                backtracking(state)
                state.pop()

        backtracking([])
        return result

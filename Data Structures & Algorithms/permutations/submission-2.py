class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(state, exist):
            if len(state) == len(nums):
                result.append(state[:])
            else:
                for i in range(len(nums)):
                    if not exist[i]:
                        exist[i] = True
                        state.append(nums[i])
                        backtracking(state, exist)
                        exist[i] = False
                        state.pop()

        backtracking([], [False] * len(nums))
        return result
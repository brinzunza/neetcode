class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtracking(start, state):
            result.append(state[:])

            if len(state) >= len(nums):
                return

            for num in range(start, len(nums)):
                if num > start and nums[num] == nums[num - 1]:
                    continue
                state.append(nums[num])
                backtracking(num + 1, state)
                state.pop()

        backtracking(0, [])
        return result
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def recurse(state):
            if state >= len(nums):
                return 0

            if state in dp:
                return dp[state]

            dp[state] = max(nums[state] + recurse(state + 2), recurse(state + 1))
            return dp[state]

        return recurse(0)
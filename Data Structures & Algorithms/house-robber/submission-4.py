class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(state):
            if state == len(nums):
                return 0

            if state > len(nums):
                return 0

            if state in dp:
                return dp[state]

            # rob current and skip next, skip current
            dp[state] = max(nums[state] + dfs(state + 2), dfs(state + 1))
            return dp[state]

        return dfs(0)
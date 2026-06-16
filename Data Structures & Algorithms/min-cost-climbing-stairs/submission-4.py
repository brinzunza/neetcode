class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        n = len(cost)

        def recurse(state):
            if state >= n:
                return 0

            if state in dp:
                return dp[state]

            dp[state] = cost[state] + min(recurse(state + 1),recurse(state + 2))
            return dp[state]

        return min(recurse(0), recurse(1))

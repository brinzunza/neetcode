class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def climb(state):
            if state == len(cost):
                return 0

            if state > len(cost):
                return 0

            if state in dp:
                return dp[state]

            # cost of current plus either i + 1 or i + 2
            dp[state] = cost[state] + min(climb(state + 1), climb(state + 2))
            return dp[state]

        return min(climb(0), climb(1))
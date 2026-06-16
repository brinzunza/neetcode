class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, len(cost) + 1):
            cost_one = dp[i - 1] + cost[i - 1]
            cost_two = dp[i - 2] + cost[i - 2]
            dp[i] = min(cost_one, cost_two)

        return dp[-1]
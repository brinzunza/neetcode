class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        
        dp = [0] * (n + 1)
                
        for i in range(2, n + 1):
            cost_from_one_step = dp[i-1] + cost[i-1]
            cost_from_two_steps = dp[i-2] + cost[i-2]
            
            dp[i] = min(cost_from_one_step, cost_from_two_steps)
            
        return dp[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]
        dp.append(1)
        dp.append(2)

        for i in range(3, n+1):
            dp.append(dp[-1] + dp[-2])

        return dp[n]
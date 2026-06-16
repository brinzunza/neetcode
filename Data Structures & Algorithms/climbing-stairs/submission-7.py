class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def climb(state):
            if state == n:
                return 1
            
            if state > n:
                return 0

            if state in dp:
                return dp[state]

            dp[state] = climb(state + 1) + climb(state + 2)
            return dp[state]

        return climb(0)
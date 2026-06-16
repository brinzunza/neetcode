class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def recurse(state):
            if state == n:
                return 1
            if state > n: 
                return 0
            
            if dp.get(state, -1) != -1:
                return dp[state]

            dp[state] = recurse(state + 1) + recurse(state + 2)
            return dp[state]

        return recurse(0)
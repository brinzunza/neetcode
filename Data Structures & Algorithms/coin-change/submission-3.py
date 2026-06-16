class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(state):
            if state == 0:
                return 0
            if state < 0:
                return float('inf')

            if state in dp:
                return dp[state]

            dp[state] = 1 + min(dfs(state - c) for c in coins)
            return dp[state]

        ans = dfs(amount)
        return ans if ans != float('inf') else -1

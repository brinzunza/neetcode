"""
input: integer array coins (empty? values? negatives? always valid solution?) : integer amount (value? negative? always valid solution?)
output: integer; represents the fewest number of coins needed to add up to the exact amount

brute force: use a tree where for each coin, you either choose to use it or you don't 

optimal: dynamic programming: 
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i):
            if i == 0:
                return 0
            if i in dp:
                return dp[i]

            result = 1e9
            for coin in coins:
                if i - coin >= 0:
                    result = min(result, 1 + dfs(i - coin))

            dp[i] = result
            return result

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
            
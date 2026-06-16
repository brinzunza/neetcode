"""
each index in dp is the number of coins
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]

            fewest = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    fewest = min(fewest, 1 + dfs(amount - coin))

            dp[amount] = fewest
            return fewest

        minCoins = dfs(amount)
        if minCoins == 1e9:
            return -1
        return minCoins
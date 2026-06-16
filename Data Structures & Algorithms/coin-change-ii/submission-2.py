class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(total, i):
            if total == 0:
                return 1
            if total < 0:
                return 0

            if (total, i) in dp:
                return dp[(total, i)]

            ways = 0
            for c in range(i, len(coins)):
                ways += dfs(total - coins[c], c)

            dp[(total, i)] = ways
            return ways

        return dfs(amount, 0)

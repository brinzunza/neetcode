class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in dp:
                return dp[(i, holding)]

            if holding:
                dp[(i, holding)] = max(prices[i] + dfs(i + 2, 0), dfs(i + 1, 1))
            else:
                dp[(i, holding)] = max(-prices[i] + dfs(i + 1, 1), dfs(i + 1, 0))

            return dp[(i, holding)]

        return dfs(0, 0)

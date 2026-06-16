"""
input: int array prices
output: int, maximum distance from buy to sell (profit)

have a sliding window to keep track of what is the furthest distance a day can go. Adjust day if no longer can go.
Keep track of the largest available window
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2):
            return 0
        wStart = 0
        wEnd = 1
        maxProfit = 0
        while(wEnd <= len(prices) - 1):
            if prices[wEnd] < prices[wStart]:
                wStart = wEnd
                wEnd = wStart + 1
            else:
                profit = prices[wEnd] - prices[wStart]
                if profit > maxProfit:
                    maxProfit = profit
                wEnd += 1

        return maxProfit

"""
Time complexity: O(n)
Space complexity: O(1)
"""
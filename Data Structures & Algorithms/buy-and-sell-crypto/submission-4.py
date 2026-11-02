class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        smallest = prices[0]

        for price in prices:
            if price - smallest > result:
                result = price - smallest
            if price < smallest:
                smallest = price

        return result
"""
input: integer array prices (empty? values?)
output: integer that represents the largest profit we can make 

1. for every day, find the largest future day and keep track of largest profit. t: O(n^2) s: O(1)

2. keep track of current smallest seen and for everyday see if the current day is the largest we've seen. t: O(n) s: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        smallest = prices[0]

        for i in prices:
            result = max(result, i - smallest)
            smallest = min(smallest, i)

        return result
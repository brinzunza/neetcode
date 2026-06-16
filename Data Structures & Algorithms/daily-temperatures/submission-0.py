"""
input: int array temperatures, temperatures i is daily temp on ith day
output: int array result, result i is num of days until warmer temp in future

array? 0?, temperatures? negative?

use a stack to keep track of which temperatures still have not found a day warmer. Since temperatures only get lower, then stack works. 
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]:
                prev_index, prev_temp = stack.pop()
                days[prev_index] = i - prev_index
            stack.append((i, temp))

        return days

"""
Time complexity: O(n)
Space complexity: O(n)
"""

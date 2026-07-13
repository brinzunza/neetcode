"""
input: integer array temperatures (len? empty? values?)
output: integer array; represents the days left before reaching a warmer day

1. for each value, iterate through original array and find the higher day; t: O(n^2) s: O(n)

2. keep a monotonic stack of temperatures plus their original location and once a hotter day comes pop it and subtract current day vs orignal day
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                day, _ = stack.pop()
                result[day] = i - day
            stack.append((i, temp))

        return result

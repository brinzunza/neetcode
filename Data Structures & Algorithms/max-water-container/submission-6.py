"""
input: integer array heights (empty? size? decimals?)
output: integer; represents the largest area enclosed by a rectangle by two bars from heights[i]

1. for each bar, compare to every other bar keeping track of the largest area that has been seen
    t: O(n^2) s: O(1)

2. use two pointers from the outer two bars covering the longest distance and move them relative to the next bar that would return the next largest area
    t: O(n) s: O(1)

1,7,2,5,4,7,3,6
  1           1
36
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        result = 0
        while(start < end):
            result = max(result, (end - start) * min(heights[start], heights[end]))
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return result 
        
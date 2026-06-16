"""
inputs: heights= array of ints
outputs: int = max amount of area between two bars

what if a height is 0
what if the array is empty
how large can these numbers be
how large can the array be 
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxSpace = 0
        start = 0
        end = len(heights) - 1

        while start != end:
            if(heights[start] > heights[end]):
                currArea = heights[end] * (end - start)
                end -= 1
            else:
                currArea = heights[start] * (end - start)
                start += 1
            if(currArea > maxSpace):
                maxSpace = currArea

        return maxSpace
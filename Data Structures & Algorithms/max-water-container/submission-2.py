"""
input: int array heights 
output: int, max water you can store, distance x height

heights len? 0? 
range of heights?

one pointer at start, one at end, keep track of largest so far, move smaller height of pointer closer until they meet. 
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        most_water = 0

        while(start < end):
            curr_water = 0
            if(heights[start] < heights[end]):
                curr_water = (end - start) * heights[start]
                start += 1
            else:
                curr_water = (end - start) * heights[end]
                end -= 1
            if(curr_water > most_water):
                most_water = curr_water
        
        return most_water

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
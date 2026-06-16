"""
input: int array height
output: int, max area of water

can water be trapped with edges?
len of height? 0?

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_left = height[start]
        max_right = height[end]
        water = 0
        while(start < end):
            if(height[start] < height[end]):
                start += 1
                max_left = max(max_left, height[start])
                water += max_left - height[start]
            else:
                end -= 1
                max_right = max(max_right, height[end])
                water += max_right - height[end]

        return water

"""
Time complexity: O(n)
Space Complexity: O(1)
"""
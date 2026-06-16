"""
input: int array heights
output: int, area of largest rectangle that can be formed 

since heights have to be same or increasing to continue right, we can use a stack to control how long they can be. Keep track of largest size and pop until curr is greater than or eequal to top of stack. 
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i in range(len(heights) + 1):
            if (i == len(heights)):
                curr_height = 0
            else:
                curr_height = heights[i]

            if (len(stack) == 0 or curr_height >= heights[stack[-1]]):
                stack.append(i)
            else:
                while len(stack) > 0 and curr_height < heights[stack[-1]]:
                    top = stack.pop()
                    height = heights[top]
                    if len(stack) == 0:
                        width = i
                    else:
                        width = i - stack[-1] - 1
                    area = height * width
                    if area > largest:
                        largest = area
                stack.append(i)
        return largest

"""
Time complexity: O(n^2)
Space complexity: O(n)
"""
"""
input: integer array height (nonnegative, len?, empty?)
output: integer that represents the maximum amount of water that can be trapped within the bars. 

1. for row track bars and open areas and add to total. t: O(n * max(n)) s: O(1)

2. track highest bar from both left and right sides and for each index keep the min - the height of current index. t: O(n) s: O(n)

[0,2,0,3,1,0,1,3,2,1]

left = [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
right = [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]
9
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        leftHeights = [0] * n
        rightHeights = [0] * n

        for i in range(1, n):
            leftHeights[i] = max(leftHeights[i - 1], height[i - 1])

        for i in range(n - 2, 0, -1):
            rightHeights[i] = max(rightHeights[i + 1], height[i + 1])

        for i in range(n):
            total = min(leftHeights[i], rightHeights[i]) - height[i]
            if(total > 0):
                result += total

        return result

        
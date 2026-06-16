class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        hleft = [0] * n
        hright = [0] * n

        for i in range(1, n):
            hleft[i] = max(hleft[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            hright[i] = max(hright[i + 1], height[i + 1])

        result = 0
        for i in range(n):
            water = min(hleft[i], hright[i]) - height[i]
            if water > 0:
                result += water

        return result

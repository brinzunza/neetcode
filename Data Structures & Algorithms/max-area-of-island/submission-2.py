class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    size = 0
                    grid[i][j] = -1
                    while stack:
                        a, b = stack.pop()
                        size += 1

                        if a + 1 < len(grid) and grid[a + 1][b] == 1:
                            stack.append((a + 1, b))
                            grid[a + 1][b] = -1
                        if b + 1 < len(grid[0]) and grid[a][b + 1] == 1:
                            stack.append((a, b + 1))
                            grid[a][b + 1] = -1
                        if a > 0 and grid[a - 1][b] == 1:
                            stack.append((a - 1, b))
                            grid[a - 1][b] = -1
                        if b > 0 and grid[a][b - 1] == 1:
                            stack.append((a, b - 1))
                            grid[a][b - 1] = -1

                    result = max(result, size)

        return result
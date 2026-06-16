from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0

        def dfs(grid, row, col):
            size = 0
            stack = [(row, col)]
            grid[row][col] = 0
            maxRow = len(grid)
            maxCol = len(grid[0])

            while stack:
                size += 1
                row, col = stack.pop()

                if row + 1 < maxRow and grid[row + 1][col] == 1:
                    stack.append((row + 1, col))
                    grid[row + 1][col] = 0
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    stack.append((row - 1, col))
                    grid[row - 1][col] = 0
                if col + 1 < maxCol and grid[row][col + 1] == 1:
                    stack.append((row, col + 1))
                    grid[row][col + 1] = 0
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    stack.append((row, col - 1))
                    grid[row][col - 1] = 0

            return size

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    size = dfs(grid, row, col)
                    if size > maxIsland:
                        maxIsland = size
        
        return maxIsland
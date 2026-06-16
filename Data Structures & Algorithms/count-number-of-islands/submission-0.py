class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0

        def dfs(grid, i, j):
            rows, cols = len(grid), len(grid[0])
            stack = [[i, j]]
            grid[i][j] = '0'

            while stack:
                row, col = stack.pop()

                if row > 0 and grid[row - 1][col] == '1':
                    stack.append([row - 1, col])
                    grid[row - 1][col] = '0'
                if row < rows - 1 and grid[row + 1][col] == '1':
                    stack.append([row + 1, col])
                    grid[row + 1][col] = '0'
                if col > 0 and grid[row][col - 1] == '1':
                    stack.append([row, col - 1])
                    grid[row][col - 1] = '0'
                if col < cols - 1 and grid[row][col + 1] == '1':
                    stack.append([row, col + 1])
                    grid[row][col + 1] = '0'

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(grid, row, col)
        
        return islands
"""
input: 2d string array grid (only chars 0 and 1, square? empty?)
output: integer; represents the number of islands that exist ie surrounded by water

1. keep a map of groups that are next to each other keeping their positions. disjoint set union

2. iterate through each position, when 1 is found use dfs or bfs to find how large that island is. 
"""

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    stack = []
                    stack.append((i, j))
                    while stack:
                        x, y = stack.pop()
                        grid[x][y] = '2'

                        if len(grid) > x + 1 and grid[x + 1][y] == '1':
                            grid[x + 1][y] = '2'
                            stack.append((x + 1, y))
                        if x > 0 and grid[x - 1][y] == '1':
                            grid[x - 1][y] = '2'
                            stack.append((x - 1, y))
                        if len(grid[0]) > y + 1 and grid[x][y + 1] == '1':
                            grid[x][y + 1] = '2'
                            stack.append((x, y + 1))
                        if y > 0 and grid[x][y - 1] == '1':
                            grid[x - 1][y] = '2'
                            stack.append((x, y - 1))

                    islands += 1

        return islands

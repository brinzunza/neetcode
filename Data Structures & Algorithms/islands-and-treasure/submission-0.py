"""
input: grid 2d array of ints
output: grid 2d array of ints

approach: start at each 0, breadth first search to all possible nodes and update distance if less than current
- 
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            i, j, dist = queue.popleft()
            if grid[i][j] > dist:
                grid[i][j] = dist

            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] > dist + 1:
                    queue.append((x, y, dist + 1))

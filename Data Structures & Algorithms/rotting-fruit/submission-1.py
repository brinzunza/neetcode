"""
for each rotten fruit do a breadth first search and edit the value to the distance away

then find the cell with the highest value representing the point furthest from all other points. 
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        queue = deque()
        level = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    level.append((i, j))

        if level:
            queue.append(level)

        while queue:
            current = queue.popleft()
            level = []

            for i in current:
                a, b = i[0], i[1]

                if a + 1 < len(grid) and grid[a + 1][b] == 1:
                    level.append((a + 1, b))
                    grid[a + 1][b] = 2

                if b + 1 < len(grid[0]) and grid[a][b + 1] == 1:
                    level.append((a, b + 1))
                    grid[a][b + 1] = 2

                if a > 0 and grid[a - 1][b] == 1:
                    level.append((a - 1, b))
                    grid[a - 1][b] = 2

                if b > 0 and grid[a][b - 1] == 1:
                    level.append((a, b - 1))
                    grid[a][b - 1] = 2

            if level:
                queue.append(level)
                result += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return result

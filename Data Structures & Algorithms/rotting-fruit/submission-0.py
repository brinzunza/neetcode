class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        totalFresh = 0
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    totalFresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        while queue:
            i, j, time = queue.popleft()
            minutes = max(minutes, time)

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = 2
                    totalFresh -= 1
                    queue.append((x, y, time + 1))

        if totalFresh > 0:
            return -1
        return minutes

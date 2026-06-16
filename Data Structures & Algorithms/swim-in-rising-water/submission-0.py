from heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        pq = []
        heappush(pq, (grid[0][0], 0, 0))
        visited = set()
        
        while pq:
            time, i, j = heappop(pq)
            
            if (i, j) in visited:
                continue
            visited.add((i, j))
            
            if i == n - 1 and j == n - 1:
                return time

            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    new_time = max(time, grid[x][y])
                    heappush(pq, (new_time, x, y))

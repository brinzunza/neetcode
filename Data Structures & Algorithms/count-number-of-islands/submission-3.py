
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    stack = [(i, j)]

                    while stack:
                        a, b = stack.pop()

                        if grid[a][b] == "1":
                            grid[a][b] = "0"

                            if a + 1 < len(grid) and grid[a + 1][b] == "1":
                                stack.append((a + 1, b))

                            if a - 1 >= 0 and grid[a - 1][b] == "1":
                                stack.append((a - 1, b))

                            if b + 1 < len(grid[0]) and grid[a][b + 1] == "1":
                                stack.append((a, b + 1))

                            if b - 1 >= 0 and grid[a][b - 1] == "1":
                                stack.append((a, b - 1))

                    total_islands += 1

        return total_islands

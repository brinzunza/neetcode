class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtracking(i, j, index):
            if index == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"  

            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                if backtracking(i + dx, j + dy, index + 1):
                    board[i][j] = temp
                    return True

            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if backtracking(i, j, 0):
                    return True

        return False

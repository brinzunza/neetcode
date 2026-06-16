"""
input: 2d integer array board (empty? always a valid solution?)
output: boolean; represents if the current state (not future) of the sodoku board is valid or abiding by its rules

1. go through each index checking: valid row, valid col, valid square O(n^2 * 3n) = O(n^3)
 - keep cache of already checked rows and cols and squares
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            visited = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in visited:
                    return False
                visited[board[i][j]] = 1
        #cols
        for i in range(9):
            visited = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in visited:
                    return False
                visited[board[j][i]] = 1
        #squares
        for i in range(9):
            visited = {}
            for j in range(3):
                for k in range(3):
                    row = (i//3) * 3 + j
                    col = (i % 3) * 3 + k
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in visited:
                        return False
                    visited[board[row][col]] = 1

        return True
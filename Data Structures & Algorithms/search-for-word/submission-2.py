"""
go through each index of 2d array, if we find char that matches first letter, check each of the 4 neighbors to see if it continues, if found return True, if none return False
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def traverse(i, j, curr):
            if board[i][j] != word[curr]:
                return False

            if curr == len(word) - 1:
                return True

            temp = board[i][j]
            board[i][j] = "#"

            if i + 1 < len(board):
                if traverse(i + 1, j, curr + 1):
                    board[i][j] = temp
                    return True

            if j + 1 < len(board[0]):
                if traverse(i, j + 1, curr + 1):
                    board[i][j] = temp
                    return True

            if i - 1 >= 0:
                if traverse(i - 1, j, curr + 1):
                    board[i][j] = temp
                    return True

            if j - 1 >= 0:
                if traverse(i, j - 1, curr + 1):
                    board[i][j] = temp
                    return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if traverse(i, j, 0):
                    return True

        return False

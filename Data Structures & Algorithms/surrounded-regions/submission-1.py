
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        stack = [(i, j)]
                        board[i][j] = "S"

                        while stack:
                            row, col = stack.pop()

                            if row + 1 < len(board) and board[row + 1][col] == "O":
                                stack.append((row + 1, col))
                                board[row + 1][col] = "S"

                            if col + 1 < len(board[0]) and board[row][col + 1] == "O":
                                stack.append((row, col + 1))
                                board[row][col + 1] = "S"

                            if row > 0 and board[row - 1][col] == "O":
                                stack.append((row - 1, col))
                                board[row - 1][col] = "S"

                            if col > 0 and board[row][col - 1] == "O":
                                stack.append((row, col - 1))
                                board[row][col - 1] = "S"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    board[i][j] = "O"

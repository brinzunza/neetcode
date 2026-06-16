class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.backtracking(board, word, i, j, 0):
                    return True
        return False

    def backtracking(self, board, word, row, col, index):
        if index == len(word):
            return True
        
        if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = '#'
        
        result = self.backtracking(board, word, row + 1, col, index + 1) or self.backtracking(board, word, row - 1, col, index + 1) or self.backtracking(board, word, row, col + 1, index + 1) or self.backtracking(board, word, row, col - 1, index + 1)

        board[row][col] = temp
        
        return result
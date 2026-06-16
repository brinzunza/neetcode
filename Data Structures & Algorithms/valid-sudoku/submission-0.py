"""
input: list of int lists board
output: boolean, true if valid soduku board, else false

make rows into sets and check if duplicates
make cols into sets and check if duplicates

brute force 3x3 cells
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9): 
            map = {}
            for i in range(9):
                if(board[row][i] != '.'):
                    if board[row][i] in map:
                        print("row issue")
                        return False
                    else:
                        map[board[row][i]] = 0

        for col in range(9): 
            map = {}
            for i in range(9):
                if(board[i][col] != '.'):
                    if board[i][col] in map:
                        print("col issue")
                        return False
                    else:
                        map[board[i][col]] = 0
        
        for grid in range(9):
            map = {}
            for i in range(3):
                for j in range(3):
                    rowStart = (grid // 3) * 3 + i
                    colStart = (grid % 3) * 3 + j
                    if(board[rowStart][colStart] != '.'):
                        if(board[rowStart][colStart] in map): 
                            print("grid issue")
                            return False
                        else:
                            map[board[rowStart][colStart]] = 0

        return True
"""
input: int list board: 2d array of coordinates. size? empty?
output: none. change the board, inplace but don't return

go through all coordinates on the border and run bfs on those connected to it either up down left or right. keep track of all the coordinates it touches
then go through all coordinates not on the border and change them to an X unless they are in the previously tracked coordinates
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == 0 or r == ROWS - 1 or
                        c == 0 or c == COLS - 1 and
                        board[r][c] == "O"
                    ):
                        q.append((r, c))
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            q.append((nr, nc))

        capture()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
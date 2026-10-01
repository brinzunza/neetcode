class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        for j in range(m):
            if matrix[0][j] == 0:
                firstRowZero = True

        for i in range(n):
            if matrix[i][0] == 0:
                firstColZero = True

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0

        if firstRowZero:
            for j in range(m):
                matrix[0][j] = 0

        if firstColZero:
            for i in range(n):
                matrix[i][0] = 0
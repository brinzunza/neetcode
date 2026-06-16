"""
input: 2d integer matrix (empty? m and n always different? values? )
output: 1d integer array; represents the values of matrix in order as if forming a spiral

separate matrix by levels of perimeters with these properties
- top and bottom always stays the same
- middle arrays are only last elements and first elements
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        def getCurrentPerimeter(m):
            current = []
            if not m or not m[0]:
                return current

            # top row
            current.extend(m[0])

            # right column (excluding first and last row)
            for i in range(1, len(m) - 1):
                current.append(m[i][-1])

            # bottom row (if more than one row)
            if len(m) > 1:
                current.extend(m[-1][::-1])  # include last element before reversing

            # left column (if more than one column)
            if len(m[0]) > 1:
                for i in range(len(m) - 2, 0, -1):
                    current.append(m[i][0])

            return current

        layers = min(len(matrix), len(matrix[0])) // 2 + (min(len(matrix), len(matrix[0])) % 2)
        for i in range(layers):
            submatrix = [row[i:len(matrix[0]) - i] for row in matrix[i:len(matrix) - i]]
            result.extend(getCurrentPerimeter(submatrix))

        return result
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top= left
                bottom = right

                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft
            
            right -= 1
            left += 1
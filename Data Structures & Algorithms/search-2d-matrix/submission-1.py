class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        sc, ec = 0, len(matrix)

        while sc < ec:
            mid = sc + (ec - sc) // 2
            if matrix[mid][0] > target:
                ec = mid
            else:
                sc = mid + 1

        row = sc - 1
        if row < 0:
            return False

        sr, er = 0, len(matrix[row])

        while sr < er:
            mid2 = sr + (er - sr) // 2
            if matrix[row][mid2] == target:
                return True
            elif matrix[row][mid2] > target:
                er = mid2
            else:
                sr = mid2 + 1

        return False

"""
input: 2d int array matrix, int target
output: boolean, true if target exists in array, false otherwise

size of array matrix? 0?
size of target? always valid solution?

go through rows to see which row its between, then go into the row and find if it exists inside. 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        for row in matrix:
            if row[0] <= target <= row[-1]:
                start = 0
                end = len(row) - 1
                while start <= end:
                    half = (start + end) // 2
                    if row[half] == target:
                        return True
                    elif target > row[half]:
                        start = half + 1
                    else:
                        end = half - 1
                return False
        return False

"""
Time complexity: O(log(m * n))
Space complexity: O(1)
"""
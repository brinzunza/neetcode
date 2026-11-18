class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        accessiblePacific = set()
        accessibleAtlantic = set()

        for i in range(cols):
            stack = [(0, i)]

            while stack:
                row, col = stack.pop()

                if (row, col) in accessiblePacific:
                    continue

                accessiblePacific.add((row, col))

                if col + 1 < cols and heights[row][col + 1] >= heights[row][col]:
                    stack.append((row, col + 1))
                if col > 0 and heights[row][col - 1] >= heights[row][col]:
                    stack.append((row, col - 1))
                if row + 1 < rows and heights[row + 1][col] >= heights[row][col]:
                    stack.append((row + 1, col))
                if row > 0 and heights[row - 1][col] >= heights[row][col]:
                    stack.append((row - 1, col))

        for i in range(rows):
            stack = [(i, 0)]

            while stack:
                row, col = stack.pop()

                if (row, col) in accessiblePacific:
                    continue

                accessiblePacific.add((row, col))

                if col + 1 < cols and heights[row][col + 1] >= heights[row][col]:
                    stack.append((row, col + 1))
                if col > 0 and heights[row][col - 1] >= heights[row][col]:
                    stack.append((row, col - 1))
                if row + 1 < rows and heights[row + 1][col] >= heights[row][col]:
                    stack.append((row + 1, col))
                if row > 0 and heights[row - 1][col] >= heights[row][col]:
                    stack.append((row - 1, col))

        for i in range(cols):
            stack = [(rows - 1, i)]

            while stack:
                row, col = stack.pop()

                if (row, col) in accessibleAtlantic:
                    continue

                accessibleAtlantic.add((row, col))

                if col + 1 < cols and heights[row][col + 1] >= heights[row][col]:
                    stack.append((row, col + 1))
                if col > 0 and heights[row][col - 1] >= heights[row][col]:
                    stack.append((row, col - 1))
                if row + 1 < rows and heights[row + 1][col] >= heights[row][col]:
                    stack.append((row + 1, col))
                if row > 0 and heights[row - 1][col] >= heights[row][col]:
                    stack.append((row - 1, col))

        for i in range(rows):
            stack = [(i, cols - 1)]

            while stack:
                row, col = stack.pop()

                if (row, col) in accessibleAtlantic:
                    continue

                accessibleAtlantic.add((row, col))

                if col + 1 < cols and heights[row][col + 1] >= heights[row][col]:
                    stack.append((row, col + 1))
                if col > 0 and heights[row][col - 1] >= heights[row][col]:
                    stack.append((row, col - 1))
                if row + 1 < rows and heights[row + 1][col] >= heights[row][col]:
                    stack.append((row + 1, col))
                if row > 0 and heights[row - 1][col] >= heights[row][col]:
                    stack.append((row - 1, col))

        return [[row, col] for row, col in accessiblePacific & accessibleAtlantic]
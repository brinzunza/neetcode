"""
input: int n 
output: str array, all valid combinations of parantheses

size n?
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [['(', 1, 1]]

        while len(result[0][0]) < 2 * n:
            for i in range(len(result)):
                s, bal, opened = result[i]
                if opened < n:
                    result.append([s + '(', bal + 1, opened + 1])
                if bal > 0:
                    result[i][0] = s + ')'
                    result[i][1] = bal - 1
                else:
                    result[i] = None
            result = [r for r in result if r]

        return [r[0] for r in result if r[1] == 0]

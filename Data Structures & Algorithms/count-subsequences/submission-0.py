class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def recurse(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = recurse(i + 1, j) + (recurse(i + 1, j + 1) if s[i] == t[j] else 0)

            return dp[(i, j)]

        return recurse(0, 0)

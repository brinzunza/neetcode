class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def dfs(curr):
            if curr >= len(s):
                result.append(partition[:])
                return

            for i in range(curr, len(s)):
                substring = s[curr:i + 1]

                if substring == substring[::-1]:
                    partition.append(substring)
                    dfs(i + 1)
                    partition.pop()

        dfs(0)
        return result

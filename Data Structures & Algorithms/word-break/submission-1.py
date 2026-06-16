class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(string):
            if string in dp:
                return dp[string]
            
            if string == "":
                dp[string] = True
                return True
            
            for i in range(1, len(string) + 1):
                if string[:i] in wordDict:
                    if dfs(string[i:]):
                        dp[string] = True
                        return True

            dp[string] = False
            return False

        result = dfs(s)
        return result

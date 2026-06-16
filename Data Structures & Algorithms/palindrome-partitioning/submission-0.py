class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.backtracking(s, results, [], 0)
        return results

    def backtracking(self, s, results, progress, index):
        if index == len(s):
            results.append(list(progress))
            return

        for i in range(index, len(s)):
            substring = s[index : i + 1]
            
            if self.palindrome(substring):
                progress.append(substring)
                self.backtracking(s, results, progress, i + 1)
                progress.pop()

    def palindrome(self, text):
        i = 0
        j = len(text) - 1
        while i < j:
            if text[i] != text[j]:
                return False
            i += 1
            j -= 1
        return True
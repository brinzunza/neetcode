"""
input: string s (len? empty? always valid solution)
output: integer; represents the number of substrings in input s that are palindromes

brute force: for each character we can either choose to include or exclude O(2^n)

optimal: two pointer, start at each character and expand outward to see if palindrome
- count itself, expand to the right and check, expand to both and check. then move to next char
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countP(s, l, r):
            result = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            return result
        
        count = 0

        # for each character expand
        for i in range(len(s)):
            count += countP(s, i, i)
            count += countP(s, i, i + 1)
        return count
"""
input: string s (chars? len? empty?)
output: integer that represents the length of the longest consecutive string of characters without a repeating character

1. find every possible substring and keep track of the longest

2. keep a set of characters as you move two pointers keeping track of the longest substring you have seen
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        result = 0
        left = 0

        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            
            letters.add(s[right])
            result = max(result, right - left + 1)

        return result
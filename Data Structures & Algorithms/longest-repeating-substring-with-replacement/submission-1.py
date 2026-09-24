"""
input: string s (len? empty? chars?), integer k (size? zero? negative?)
output: integer representing the longest substring of one distinct character after k substitutions

1. go through every possible substring, distinct characters, return largest. t: O(n^3) s: O(1)
2. keep a hash table of letters and their counts
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        result = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1

            while right - left + 1 - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
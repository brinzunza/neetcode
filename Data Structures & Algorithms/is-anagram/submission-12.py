"""
input: string s (empty? upperlowercase? length? chars?), string t (same)
output: return true if both strings have same exact characters, false otherwise

1. track all chars from one string using map, then trace the other and look up each char. r: O(2n) s: O(n)

2. for each character in first string, find first appearance in second and then delete until all match. r: O(n^2) s: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

        for char in t:
            if char not in chars:
                return False
            else:
                chars[char] -= 1

        for _, v in chars.items():
            if v != 0:
                return False

        return True                
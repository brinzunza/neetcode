"""
input: string s, string t
output: boolean, true if strings are anagrams of each other false otherwise

size of s? t?
can they be empty?
what type of chars?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
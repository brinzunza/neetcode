"""
input: string s, string t
output: boolean, true if strings are anagrams of each other false otherwise

size of s? t?
can they be empty?
what type of chars?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1
        for i in t:
            if i not in count:
                return False
            count[i] -= 1
            if count[i] < 0:
                return False
        return True

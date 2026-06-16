"""
inputs: str s1, str s2
output: bool, true if s2 contains permutation of s1, else false

size of s1? empty?
size of s2? empty?

keep window to track possible letters. grow and remove accordingly. keep track of needed letters using array.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1)
        while start + end <= len(s2):
            window = list(s2[start:start + end])
            try:
                for i in s1:
                    window.remove(i)
                return True
            except:
                pass
            start += 1
        return False

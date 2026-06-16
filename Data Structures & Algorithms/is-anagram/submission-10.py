class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1 = {}
        l2 = {}

        for i in range(len(s)):
            l1[s[i]] = l1.get(s[i], 0) + 1
            l2[t[i]] = l2.get(t[i], 0) + 1

        return l1 == l2
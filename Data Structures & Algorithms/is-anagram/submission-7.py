class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print((Counter(s)))
        print((Counter(t)))
        return Counter(s) == Counter(t)
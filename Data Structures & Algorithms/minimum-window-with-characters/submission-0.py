"""
input: string s, string t : empty? length? 
output: string; longest substring of s that includes every character in t

keep map of if character is in window; -1 if not, indice else 
keep track of current shortest window indices

move start of window to second char in window and retry until end of string
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        exist = {}
        need = {}
        for c in t:
            exist[c] = -1
            need[c] = need.get(c, 0) + 1
        start = 0
        have = 0
        need_count = len(need)
        res = ""
        count = {}
        for end in range(len(s)):
            if s[end] in need:
                count[s[end]] = count.get(s[end], 0) + 1
                if count[s[end]] == need[s[end]]:
                    have += 1
            while have == need_count:
                if not res or end - start + 1 < len(res):
                    res = s[start:end + 1]
                if s[start] in need:
                    count[s[start]] -= 1
                    if count[s[start]] < need[s[start]]:
                        have -= 1
                start += 1
        return res

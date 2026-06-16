"""
input: string s
output: int, length of longest substring of s without duplicated characters

how large and small can s be? 
what characters can exist?

keep window to track the current longest substring, until duplicate appears and you move beginning of window up. 
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) < 1):
            return 0
        if(len(s) < 2):
            return 1
        start = 0
        end = 1
        maxLen = 0
        chars = set()
        chars.add(s[start])
        while(end <= len(s) - 1):
            while(s[end] in chars):
                chars.remove(s[start])
                start += 1
            chars.add(s[end])
            if((end - start + 1) > maxLen):
                maxLen = (end - start + 1)
            end += 1
        return maxLen

"""
Time complexity: O(n)
Space complexity: O(m)
"""
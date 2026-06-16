"""
input: str s, int k
output: int, the length of longest substring after k substitutions

length of s? empty?
size of k? 0?

keep a window and map of counts
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if(len(s) < 1):
            return 0
        if(len(s) < 2):
            return 1
        count = {}
        count[s[0]] = 1
        start = 0
        end = 1
        result = 0
        while(end <= len(s) - 1):
            count[s[end]] = 1 + count.get(s[end], 0)
            while((end - start + 1) - max(count.values()) > k):
                count[s[start]] -= 1
                start += 1
            result = max(result, (end - start) + 1)
            end += 1
        return result

"""
time complexity: O(n)
space complexity: O(m)
"""
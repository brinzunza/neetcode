"""
input: string s (len? empty? case? chars?)
output: integer array; represents the lengths of the substrings 

1. track counts of chars, then start at first char and extend until all of that char is used, track other chars that happen to end up inside and also include all of theirs 
 1.2. optimized by tracking where the char ends instead of count
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = {}
        
        #gets last occurrence of each char
        for i in range(len(s) - 1, -1, -1):
            ends[s[i]] = max(ends.get(s[i], 0), i)

        #finds substrings and adds to result variable
        substrings = []
        start = 0
        end = 0
        i = 0
        while(i < len(s)):
            end = max(end, ends[s[i]])

            if i == end:
                substrings.append(s[start:end + 1])
                start = end + 1
                end = start
            i += 1

        result = []
        for sub in substrings:
            result.append(len(sub))

        return result


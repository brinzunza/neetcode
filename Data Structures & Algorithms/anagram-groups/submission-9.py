"""
input: array of strings strs (len? chars? always valid solution?)
output: 2d string array of grouped anagrams (strings with the same chars)

go through array and keep buckets of same strings
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []

        #find all anagrams and put into buckets
        anagrams = {}
        for i, word in enumerate(strs):
            curr = [0] * 26
            for j in range(len(word)):
                curr[ord(word[j]) - ord('a')] += 1

            curr = tuple(curr)
            if(curr in anagrams):
                anagrams[curr].append(word)
            else:
                anagrams[curr] = [word]

        #put buckets into arrays and add to result var
        for _, val in anagrams.items():
            result.append(val)

        return result
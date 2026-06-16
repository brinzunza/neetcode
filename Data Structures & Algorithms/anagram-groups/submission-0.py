"""
inputs: strs = array of strings
output: array of str 

group words that use the exact same letters into subarrays
final array can be any order of those substrings

can input be empty
how long can words be
lowercase vs uppercase
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            sortedWord = ''.join(sorted(i))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(i)
            else:
                anagrams[sortedWord] = [i]
        
        return list(anagrams.values())
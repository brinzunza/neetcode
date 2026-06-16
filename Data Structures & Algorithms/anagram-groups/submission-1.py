"""
input: array str strs
output: 2d array, subarrays of anagrams

array size? empty?
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in hashmap:
                hashmap[key].append(i)
            else:
                hashmap[key] = [i]
        result = []
        for i in hashmap.values():
            result.append(i)
        return result
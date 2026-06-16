"""
input: string array strs (empty? chars? upperlowercase?)
output: 2d string array; groups strings that are anagrams into sublists

1. order each string and then group the indices of those that match. r: O(N*nlogn) s: O(n)

2. create a set of each string and group the sets that match. r: O(m*n) s: O(N)
"""

class Solution:

    def counter(self, word):
        result = [0] * 26
        for char in word:
            result[ord(char) - ord('a')] += 1

        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for word in strs:
            letter_count = tuple(self.counter(word))
            sets.setdefault(letter_count, []).append(word)

        result = []
        for _, v in sets.items():
            result.append(v)

        return result
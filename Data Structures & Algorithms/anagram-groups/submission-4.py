"""
input: string array strs (uppercase vs lowercase? empty? different lengths?)
output: 2D string array; represents groups of anagrams (words using same characters)

1. for each string, get Set of characters, and compare with every other character Set, combine together in Hashtable O(n * n)
 - same implementation, but remove strings that have already been used
2. sort each word (keeping the original formation), combine into subarrays those with exactly same sorted formation O(n * n * logn)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charTable = {}

        for string in strs:
            letters = [0] * 26
            for c in string:
                letters[ord(c)-ord('a')] += 1
            letters = tuple(letters)

            if charTable.get(letters, 0) != 0:
                charTable[letters].append(string)
            else:
                charTable[letters] = [string]

        result = []
        for key, value in charTable.items():
            result.append(value)
        return result

"""
test cases

1. [] = []
2. ["google"] = ["google"]
3. ["google", "elgoog", "hello", "world"]
4. ["cow", "cows"]

["act","pots","tops","cat","stop","hat"]
"""
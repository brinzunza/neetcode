class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def counter(string):
            letters = {}
            for c in string:
                letters[c] = letters.get(c, 0) + 1
            return letters

        matching = {}

        for string in strs:
            key = frozenset(counter(string).items())
            matching[key] = matching.get(key, [])
            matching[key].append(string)

        return list(matching.values())

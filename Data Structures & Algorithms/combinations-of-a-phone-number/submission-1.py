
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dictionary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = [""]

        for i in range(len(digits)):
            curr = []
            for j in result:
                for k in dictionary[digits[i]]:
                    curr.append(j + k)
            result = curr

        return result

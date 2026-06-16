class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        results = []
        self.backtrack(results, [], digits, mapping, 0)
        return results

    def backtrack(self, results, current_combination, digits, mapping, index):
        if index == len(digits):
            results.append("".join(current_combination))
            return

        current_digit = digits[index]
        possible_letters = mapping[current_digit]
        
        for letter in possible_letters:
            current_combination.append(letter)
            self.backtrack(results, current_combination, digits, mapping, index + 1)
            current_combination.pop()
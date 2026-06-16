class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        passover = 0
        if digits[len(digits) - 1] == 9:
            passover = 1
            digits[len(digits) - 1] = 0
        else:
            digits[len(digits) - 1] += 1
            return digits
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] + passover == 10:
                digits[i] = 0
            elif passover > 0:
                digits[i] += 1
                passover = 0
        if passover == 1:
            digits.insert(0, 1)
        return digits

            

class Solution:
    def reverse(self, x: int) -> int:
        minimum = -2 ** 31
        maximum = 2 ** 31 - 1

        result = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if result > maximum // 10 or (result == maximum // 10 and digit > maximum % 10):
                return 0
            if result < minimum // 10 or (result == minimum // 10 and digit < minimum %10):
                return 0

            result = (result * 10) + digit
        return result
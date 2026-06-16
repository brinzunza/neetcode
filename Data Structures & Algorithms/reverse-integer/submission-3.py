class Solution:
    def reverse(self, x: int):
        maximum = 2 ** 31 - 1
        minimum = -2 ** 31
        result = 0

        while x != 0:
            num = int(x % 10) if x > 0 else int(x % -10)
            x = int(x / 10)

            if result > maximum // 10 or (result == maximum // 10 and num > maximum % 10):
                return 0
            if result < minimum // 10 or (result == minimum // 10 and num < minimum % 10):
                return 0

            result = result * 10 + num

        return result

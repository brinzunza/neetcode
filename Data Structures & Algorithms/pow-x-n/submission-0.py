class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        result = 1
        for i in range(abs(n)):
            result *= x

        if n < 0:
            return 1/result
        return result
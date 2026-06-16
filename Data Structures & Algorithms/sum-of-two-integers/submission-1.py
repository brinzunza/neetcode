class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        result = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            curr = abit ^ bbit ^ carry
            carry = (abit + bbit + carry) >= 2
            if curr:
                result |= (1 << i)

        if result > 0x7FFFFFFF:
            result = ~(result ^ mask)

        return result
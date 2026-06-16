class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for i in range(n + 1):
            value = i
            current = 0
            for j in range(32):
                current += 1 & value
                value = value >> 1
            result.append(current)
        
        return result

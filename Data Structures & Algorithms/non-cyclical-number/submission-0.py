class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        seen[n] = n
        current = n
        future = 0
        while(True):
            while(current > 0):
                future += (current % 10)**2
                current = current // 10

            if future == 1:
                return True
            elif seen.get(future, 0) != 0:
                return False
            seen[future] = future
            current = future
            future = 0
        return
            
"""
input: integer array piles(), integer h()
output: integer; represents the minimum bananas eaten per hour, such as that all bananas are eaten while not overlapping piles

1. start at rate of 1, test if all bananas can be eaten, if not increase speed by 1, else return O(n^2)

2. binary search the rate starting at 1 and len(piles) O(nlogm)
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = right

        def testEat(rate, piles, h):
            time = 0
            for pile in piles:
                time += (pile + rate - 1) // rate 
            return time

        while left <= right:
            mid = (left + right) // 2
            result = testEat(mid, piles, h)

            if result <= h:
                best = mid
                right = mid - 1
            else:
                left = mid + 1

        return best



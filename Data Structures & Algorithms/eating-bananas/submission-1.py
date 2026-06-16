"""
input: int array piles, int h
output: int k, rate of bananas eaten per hour to finish all the piles


"""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slowest = 1
        fastest = max(piles)
        minimum = fastest

        while slowest <= fastest:
            half = (slowest + fastest) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / half)

            if total <= h:
                minimum = half
                fastest = half - 1
            else:
                slowest = half + 1

        return minimum

"""
Time complexity: O(nlogm)
Space complexity: O(1)
"""
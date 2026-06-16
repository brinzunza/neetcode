"""
input: integer array hand (empty? len? values? always a valid solution?)
output: boolean; represents true if values can be distributed into different arrays where the values only difference by one by their neighbors

1. backtracking. testing all possible permutations of different arrays

2. sort and distribute when duplicate or non + 1 value appears or limit reached.
- then keep hashmap to see which one needs which O(nlogn)

3. keep counts of nums and at each turn find smallest num. then remove groups of len k until all are done
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True
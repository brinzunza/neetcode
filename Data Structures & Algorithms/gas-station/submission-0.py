"""
input: integer array gas(), integer array cost()
output: starting index if full cycle succeeds, else -1

1. sort the stations by highest amount, then try each O(n^2)

2. find the highest amount, then use a pinter to go behind it while it increases the total, if it doesn', keep going through entire array and keep a pionter at the last known one that does increase it. this will maximize the number of distaance we can go which we know is the answer since there is at most one right answer. 
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1

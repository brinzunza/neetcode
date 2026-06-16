"""
input: integer array position(empty? always valid? negatives? len?), integer array speed(negatives? empty? always valid?), integer target(negatives? always valid?)
output: integer; represents the number of different car fleets that will arrive at the destination

1. for each car, see if it can reach next car before final, then decrease tracker of total len - 1 O(n)
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
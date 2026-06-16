"""
input: 2D integer array triplets (all valid inputs, len? always a valid solution?), integer array target(always valid solution? always ints? always len 3?)
output: boolean; represents if target triplet can be achieved by merging triplets on max function

1. start at smallest triplet, find necessary values and triplets with those, use the one with other small values, return true if valid, else false

2. start at triplet with first int as correct, then find next that is correct and merge, then last, return true if valid, else false

3. filter out triplets with values greater than target, merge all and if valid return true else false
"""

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0,0,0]
        for trip in triplets:
            x, y, z = trip
            gx, gy, gz = target
            rx, ry, rz = result
            if x <= gx and y <= gy and z <= gz:
                result = [max(rx, x), max(ry, y), max(rz, z)]

        return result == target

        
"""
test cases: 

triplets: [[1,2,3], [7,1,1]]
target: [7,2,3]

triplets: [[2,5,6],[1,4,4],[5,7,5]]
target: [5,4,6]

triplets: [[1,2,3], [4,2,1], [4,5,5]]
target: [4,2,3]
"""
"""
input: int array positions, int array speed, target
output: int possibilites

size of each input? 0? 
size of target? 0?

for i until target
    add speed to each
    if new position greater than in front
        go to infront's position

int result = 0
for i in positions going backwards
    calculate how many iterations until target
        if first or more than ahead: then add 1 to result
        else: if less than ahead, continue since its in same fleet
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 0
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            hours = (target - pos) / spd
            if len(stack) > 0 and hours <= stack[-1]:
                continue
            else:
                result += 1
                stack.append(hours)

        return result

"""
Time complexity: O(n)
Space complexity: O(n)
"""
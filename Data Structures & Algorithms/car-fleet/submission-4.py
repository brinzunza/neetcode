class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        for i in range(len(position)):
            fleet.append([position[i], speed[i]])

        fleet.sort(key=lambda k: k[0])

        result = 0

        while fleet:
            pos, sp = fleet.pop()
            time = (target - pos) / sp

            while fleet:
                prev_pos, prev_sp = fleet[-1]
                prev_time = (target - prev_pos) / prev_sp

                if prev_time <= time:
                    fleet.pop()
                else:
                    break

            result += 1

        return result

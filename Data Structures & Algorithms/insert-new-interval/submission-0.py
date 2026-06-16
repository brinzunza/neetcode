class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        i = 0
        final = []

        while i < length and intervals[i][1] < newInterval[0]:
            final.append(intervals[i])
            i += 1

        while i < length and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        final.append(newInterval)

        while i < length:
            final.append(intervals[i])
            i += 1

        return final
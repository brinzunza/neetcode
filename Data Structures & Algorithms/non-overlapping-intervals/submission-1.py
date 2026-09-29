class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        result = 0
        previousEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= previousEnd:
                previousEnd = intervals[i][1]
            else:
                result += 1
                previousEnd = min(previousEnd, intervals[i][1])

        return result
            


"""
input: tuple array intervals (len? empty? values? negatives?)
output: integer; represents the minimum number of days needed to fit all schedules

brute force: for each interval you can either choose to include it or not, O(2^n)

optimal: checking for layers of overlapping at a single time, if there exists a time with x layers of overlaps, it will require x days to complete
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if(len(intervals)) < 1:
            return 0
        starttime = [interval.start for interval in intervals]
        endtime = [interval.end for interval in intervals]
        starttime.sort()
        endtime.sort()
        startpointer = 0
        endpointer = 0
        count = 0
        result = 1
        while(startpointer < len(starttime)):
            if starttime[startpointer] < endtime[endpointer]:
                count += 1
                startpointer += 1
            else:
                endpointer += 1
                count -= 1
            result = max(result, count)
        return result
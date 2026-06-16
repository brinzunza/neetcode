"""
input: tuple array intervals (len? empty? values? negatives?)
output: boolean: represents if all meetings can be scheduled without conflicts/overlapping

brute force: for each meeting, compare to every other meeting and check if conflict

optimal: sort meetings and check if end of current affects start of next
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda k:k.start)
        prevEnd = intervals[0].end

        for interval in intervals[1:]:
            if interval.start >= prevEnd:
                prevEnd = interval.end
            else:
                return False

        return True
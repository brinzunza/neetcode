"""
input: integer 2D array intervals (len? empty? values? negatives?)
output: integer; represents minimum number of intervals we need to remove to have no overlapping intervals

brute force: iterate through each interval and at each interval we choose either to keep or delete. Runtime O(2^n)

optimal: greedy to find and keep earliest end date from those overlapped
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        #sort by start times
        intervals.sort(key=lambda k:k[0])
        prevEnd = intervals[0][1]

        #go through each interval and compare to previous end time
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            #add to counter if removal needed
            else:
                result += 1
                prevEnd = min(prevEnd, intervals[i][1])

        return result
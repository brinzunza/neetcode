"""
sort intervals first by their starting value and then by their length

[[1,3],[2,3],[3,7],[6,6]]
[[1,3]]

[2,3,1,7,6,8]

[-1, -1, -1, -1, -1, -1]

[2,2,3,5,1,-1]
"""

import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        updatedQ = []
        for i, val in enumerate(queries):
            updatedQ.append([val, i])

        updatedQ.sort()

        result = [-1] * len(queries)
        heap = []
        i = 0
        for val, pos in updatedQ:
            while i < len(intervals) and intervals[i][0] <= val:
                start, end = intervals[i]
                length = end - start + 1
                heapq.heappush(heap, (length, end))
                i += 1

            while heap and heap[0][1] < val:
                heapq.heappop(heap)

            if heap:
                result[pos] = heap[0][0]

        return result
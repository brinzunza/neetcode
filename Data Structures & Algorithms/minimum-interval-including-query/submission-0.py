"""
input: 2D integer array intervals (len? empty? values? negatives?), integer array queries(len? empty? values? always valid solution?)
output: integer array; represents query output based on 

brute force: for each query, check each interval to see if in and if so, track smallest interval O(n^2)

optimal: sort intervals and queries and use two pointer to find shortest 
- for first query find smallest that satisfies, the next query should be at earliest that one if not a future one that we have not seen
"""

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda k: k[0])
        for i, value in enumerate(queries):
            queries[i] = [value, i]
        queries.sort(key=lambda k: k[0])
        res = [-1] * len(queries)
        h = []
        ipointer = 0

        for q, idx in queries:
            while ipointer < len(intervals) and intervals[ipointer][0] <= q:
                l, r = intervals[ipointer]
                heapq.heappush(h, (r - l + 1, r))
                ipointer += 1
            while h and h[0][1] < q:
                heapq.heappop(h)
            if h:
                res[idx] = h[0][0]
        return res
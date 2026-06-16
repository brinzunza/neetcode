"""
inputs: points, 2D array of sets of coordinates (size of array?, size of int?), k, int of the top k nearest to the origin (k less than size of array? k = 0?)
output: 2d array of points of length k
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            distances.append((((p[0]-0)**2 + (p[1]-0)**2)**0.5, p[0], p[1]))

        heapq.heapify(distances)
        
        result = []
        for i in range(k):
            point = heapq.heappop(distances)
            result.append([point[1], point[2]])

        return result

"""
time complexity: O(nlogn)
space complexity: O(n)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            distances.append((((p[0]-0)**2 + (p[1]-0)**2)**0.5, p[0], p[1]))

        distances.sort(key=lambda x: x[0])
        
        result = []
        for i in range(k):
            result.append([distances[i][1], distances[i][2]])

        return result
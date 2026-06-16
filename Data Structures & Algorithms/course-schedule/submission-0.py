"""
inputs: int numCourses: number of courses that you are required to take, int list prerequisites: 2d array of arrays that shows what class 0, needs what requirement class 1. size? empty? always possible?
output: True if it is possible to finish all courses, otherwise False

for each class, track prereqs in adjacency list
then iterate for each class in adjacency list run dfs to see if class can be complete and modify adjacency list if it can
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
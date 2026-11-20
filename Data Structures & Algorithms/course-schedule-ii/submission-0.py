"""
for each course, keep array of courses it unlocks
each course keeps a count of how many unlocks it needs
keep a queue to find ordering
return ordering
"""

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        reqs = {}
        need = {}

        for i in range(numCourses):
            reqs[i] = []
            need[i] = 0

        for course, before in prerequisites:
            reqs[before].append(course)
            need[course] += 1

        queue = deque()

        for course, count in need.items():
            if count == 0:
                queue.append(course)

        while queue:
            current = queue.popleft()
            result.append(current)

            for course in reqs[current]:
                need[course] -= 1

                if need[course] == 0:
                    queue.append(course)

        if len(result) == numCourses:
            return result

        return []
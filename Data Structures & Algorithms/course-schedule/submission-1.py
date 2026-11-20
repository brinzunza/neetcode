class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        totalNeed = {}

        for i in range(numCourses):
            courses[i] = []
            totalNeed[i] = 0

        for a, b in prerequisites:
            courses[b].append(a)
            totalNeed[a] += 1

        left = numCourses
        queue = deque()

        for course, need in totalNeed.items():
            if need == 0:
                queue.append(course)

        while queue:
            current = queue.popleft()
            left -= 1

            for i in courses[current]:
                totalNeed[i] -= 1

                if totalNeed[i] == 0:
                    queue.append(i)

        return left == 0
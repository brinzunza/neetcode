"""
make an adjacency list and find 
"""


from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()
        adjacency = {}

        for i in range(n):
            adjacency[i] = []

        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        queue = deque()
        queue.append((0, None))

        while queue:
            current, parent = queue.popleft()

            if current in visited:
                return False

            visited.add(current)

            for neighbor in adjacency[current]:
                if neighbor != parent:
                    queue.append((neighbor, current))

        return len(visited) == n

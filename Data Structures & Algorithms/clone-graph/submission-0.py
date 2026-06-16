"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        visited[node] = Node(node.val)
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for i in current.neighbors:
                if i not in visited:
                    visited[i] = Node(i.val)
                    queue.append(i)
                visited[current].neighbors.append(visited[i])

        return visited[node]
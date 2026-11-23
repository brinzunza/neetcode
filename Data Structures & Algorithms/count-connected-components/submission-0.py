"""
make each of the graphs connect to one single node as the head, then count the heads
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {}

        for i in range(n):
            nodes[i] = i

        def find(node):
            if nodes[node] != node:
                nodes[node] = find(nodes[node])
            return nodes[node]

        heads = n

        for a, b in edges:
            headA = find(a)
            headB = find(b)

            if headA != headB:
                nodes[headA] = headB
                heads -= 1

        return heads
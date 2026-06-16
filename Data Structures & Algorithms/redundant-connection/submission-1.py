"""
input: 2D integer array edges (len? empty? values?)
output: 1D array; represents an edge that can be removed from the graph that keeps it an undirected graph while becoming acyclic

brute force: for each edge, run a graph traversal algorithm such as dfs, find all that can be removed and remove last 

optimal: get adjacency list of each node, traverse edges backwards and check if current last node is an edge to nodes with at least 2 incoming inputs
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(len(edges) + 1)]
        for first, second in edges:
            adjlist[first].append(second)
            adjlist[second].append(first)

        visit = [False] * (len(edges) + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if visit[node] == True:
                cycleStart = node
                return True
            
            visit[node] = True
            for n in adjlist[node]:
                if n == parent:
                    continue
                if dfs(n, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for i in range(len(edges) - 1, -1, -1):
            if edges[i][0] in cycle and edges[i][1] in cycle:
                return [edges[i][0], edges[i][1]]

        return []

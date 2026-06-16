"""
input: node p; root of first binary tree, node q; root of second binary tree : null? size of binary tree? connected?
output: boolean; true if both trees have same structure and same values, false otherwise

breadth first search going through each node and making sure that they have the same value. 
constantly check that nodes are same position (right vs left child) and value
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            nodep, nodeq = queue.popleft()
            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False
            queue.append((nodep.left, nodeq.left))
            queue.append((nodep.right, nodeq.right))
        return True

"""
time complexity: O(n)
space complexity: O(n)
"""
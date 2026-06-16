# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if(root):
            queue.append(root)

        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return depth

"""
time complexity: O(n)
space complexity: O(n)
"""
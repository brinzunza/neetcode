# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, False)]
        counter = 0

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                counter += 1
                if counter == k:
                    return node.val
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))

        return -1
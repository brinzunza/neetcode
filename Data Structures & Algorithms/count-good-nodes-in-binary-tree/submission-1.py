# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        stack = [(-101, root)]

        while stack:
            currentMax, node = stack.pop()

            if node.val >= currentMax:
                result += 1

            if node.right:
                stack.append((max(currentMax, node.val), node.right))
            if node.left:
                stack.append((max(currentMax, node.val), node.left))

        return result

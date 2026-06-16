# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, -101))
        result = 0

        while stack:
            node, highest = stack.pop()
            update = False

            if node.val >= highest:
                result += 1
                update = True

            if node.left:
                if update:
                    stack.append((node.left, node.val))
                else:
                    stack.append((node.left, highest))
            if node.right:
                if update:
                    stack.append((node.right, node.val))
                else:
                    stack.append((node.right, highest))
        return result
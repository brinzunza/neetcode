# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        values = {}

        while stack:
            node = stack[-1]
            if node.left and node.left not in values:
                stack.append(node.left)
            elif node.right and node.right not in values:
                stack.append(node.right)
            else:
                node = stack.pop()

                left = values.get(node.left, 0)
                right = values.get(node.right, 0)

                if abs(left - right) > 1:
                    return False

                values[node] = max(left, right) + 1

        return True
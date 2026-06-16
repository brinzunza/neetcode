# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        values = {None: (0,0)}

        while stack:
            node = stack[-1]
            if node.left and node.left not in values:
                stack.append(node.left)
            elif node.right and node.right not in values:
                stack.append(node.right)
            else:
                node = stack.pop()

                lheight, lmax = values[node.left]
                rheight, rmax = values[node.right]

                values[node] = (1 + max(lheight, rheight), max(lheight + rheight, lmax, rmax))

        return values[root][1]

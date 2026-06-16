"""
input: node root, root of the binary tree : empty tree? size of tree?
output: int, longest path between two nodes

use depth first search to gather information of depth of deepest nodes and update as you go back up.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = []
        stack.append(root)
        values = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in values:
                stack.append(node.left)
            elif node.right and node.right not in values:
                stack.append(node.right)
            else:
                node = stack.pop()

                lheight, ldiameter = values[node.left]
                rheight, rdiameter = values[node.right]

                values[node] = (1 + max(lheight, rheight),
                           max(lheight + rheight, ldiameter, rdiameter))

        return values[root][1]
            
"""
time complexity: O(n)
space complexity: O(n)
"""
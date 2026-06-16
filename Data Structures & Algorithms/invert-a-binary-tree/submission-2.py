"""
input: node root of tree : size of tree? empty tree?
output: node root of inverted tree

use depth first search to go through each node and invert their children's positions
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root or (not root.left and not root.right)):
            return root

        stack = [root]
        while stack:
            node = stack.pop()
            left = node.left
            right = node.right
            node.left = right
            node.right = left
            if(right):
                stack.append(right)
            if(left):
                stack.append(left)

        return root

"""
time complexity: O(n)
space complexity: O(1)
"""
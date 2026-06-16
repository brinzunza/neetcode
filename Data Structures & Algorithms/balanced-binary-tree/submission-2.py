"""
input: node, root of binary tree : size of tree? 0?
output: boolean, true if binary tree is balanced, false otherwise

use depth first search to get the leaves and compare difference of leaves
keep track of the imbalanced leaves in map and as you move back up the tree
"""

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

"""
time complexity: O(n)
space complexity: O(n)
"""
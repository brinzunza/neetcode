# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
travserse using dfs, each node is the max of its path on either left or right or both combined

keep a pointer to current max
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def dfs(node):
            nonlocal result
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            result = max(result, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return result

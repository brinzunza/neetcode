"""
input: root, node at the start of the tree (empty? size of tree?) : p, value of specific node in tree : q, value of specific node in tree (always have common ancestor?)
output: node, lowest common ancestor of both p and q(which can be p or q themselves)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while True:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

"""
time complexity: O(h)
space complexity: O(1)
"""
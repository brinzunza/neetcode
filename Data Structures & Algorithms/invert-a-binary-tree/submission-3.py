# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return

        def invert(head):
            temp = head.right
            head.right = head.left
            head.left = temp
            if head.right:
                invert(head.right)
            if head.left:
                invert(head.left)

        invert(root)

        return root
"""
inputs: root, node at start of tree (empty tree? length of tree? duplicate values?) : subroot, root of next tree (size of subtree? garaunteed to exist in other tree? empty?)
output: boolean, true if subtree exists in larger tree, false otherwise

bfs until the value of subtree's root is found in larger tree, then bfs both to check same values and structure
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def match(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            queue = deque([[n1, n2]])
            while queue:
                a, b = queue.popleft()
                if not a and not b:
                    continue
                if not (a and b):
                    return False
                if a.val != b.val:
                    return False
                queue.append([a.left, b.left])
                queue.append([a.right, b.right])
            return True

        queueFind = deque([root])
        while queueFind:
            node = queueFind.popleft()
            if node.val == subRoot.val and match(node, subRoot):
                return True
            if node.left:
                queueFind.append(node.left)
            if node.right:
                queueFind.append(node.right)

        return False
            

"""
Time complexity: O(n+m)
space complexity: O(n+m)
"""
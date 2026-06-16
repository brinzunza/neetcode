# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        current = deque([root])
        future = deque()

        result = []

        while current:
            levelNodes = []

            while current:
                node = current.popleft()
                levelNodes.append(node.val)

                if node.left:
                    future.append(node.left)
                if node.right:
                    future.append(node.right)

            result.append(levelNodes)
            current, future = future, deque()

        return result

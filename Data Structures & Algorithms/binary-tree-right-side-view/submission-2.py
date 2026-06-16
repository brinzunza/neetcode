# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        currLevel = deque()
        nextLevel = deque()
        currLevel.append(root)
        right = False
        result = []
        while currLevel or nextLevel:
            while currLevel:
                node = currLevel.popleft()

                if node.right:
                    nextLevel.append(node.right)
                if node.left:
                    nextLevel.append(node.left)
                if right == False:
                    result.append(node.val)
                    right = True
            currLevel = nextLevel
            nextLevel = deque()
            right = False
        return result
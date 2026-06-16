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
        currLevel = deque()
        currLevelVals = []
        nextLevel = deque()
        currLevel.append(root)
        result = []

        while(currLevel or nextLevel):
            while(currLevel):
                node = currLevel.popleft()
                currLevelVals.append(node.val)
                if(node.left):
                    nextLevel.append(node.left)
                if(node.right):
                    nextLevel.append(node.right)
            
            result.append(currLevelVals)
            currLevelVals = []
            currLevel = nextLevel
            nextLevel = deque()

        return result
            
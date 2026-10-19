class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(numsLeft):
            if not numsLeft:
                return None

            mid = len(numsLeft) // 2
            root = TreeNode(numsLeft[mid])
            root.left = build(numsLeft[:mid])
            root.right = build(numsLeft[mid + 1:])

            return root

        return build(nums)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(curr, idx):
            result.append(curr[:])

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(curr, i + 1)
                curr.pop()

        dfs([], 0)
        return result

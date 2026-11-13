
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(curr, idx, total):
            if total == target:
                result.append(curr[:])
                return

            for i in range(idx, len(nums)):
                if total + nums[i] > target:
                    break

                curr.append(nums[i])
                dfs(curr, i, total + nums[i])
                curr.pop()

        dfs([], 0, 0)
        return result

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(arr):
            dp = {}

            def dfs(i):
                if i >= len(arr):
                    return 0
                if i in dp:
                    return dp[i]
                dp[i] = max(dfs(i + 1), dfs(i + 2) + arr[i])
                return dp[i]

            return dfs(0)

        case1 = solve(nums[:-1])
        case2 = solve(nums[1:])

        return max(case1, case2)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(curr, idx, total):
            if total == target:
                result.append(curr[:])
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                curr.append(candidates[i])
                dfs(curr, i + 1, total + candidates[i])
                curr.pop()

        dfs([], 0, 0)
        return result

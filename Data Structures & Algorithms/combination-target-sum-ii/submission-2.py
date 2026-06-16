class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtracking(start, total, state):
            if total == target:
                result.append(state[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                state.append(candidates[i])
                backtracking(i + 1, total + candidates[i], state)
                state.pop()

        backtracking(0, 0, [])
        return result

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        stack = [(0, [], 0)]

        while stack:
            i, cur, total = stack.pop()

            if total == target:
                res.append(cur)
                continue

            if i >= len(candidates) or total > target:
                continue
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            stack.append((next_i, cur, total))

            stack.append((i + 1, cur + [candidates[i]], total + candidates[i]))

        return res
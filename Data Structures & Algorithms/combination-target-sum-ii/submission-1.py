class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtracking(start, currentSum, currentNums):
            if currentSum == target:
                result.append(currentNums[:])
                return

            if currentSum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
            
                num = candidates[i]
                currentNums.append(num)
                backtracking(i + 1, currentSum + num, currentNums)
                currentNums.pop()

        backtracking(0, 0, [])
        return result
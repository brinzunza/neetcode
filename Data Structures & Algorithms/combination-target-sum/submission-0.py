class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sets = [[]]
        
        for num in nums:
            for curr in sets:
                total = sum(curr)
                if total + num <= target:
                    sets.append(curr + [num])
        
        result = [comb for comb in sets if sum(comb) == target]
        
        return result

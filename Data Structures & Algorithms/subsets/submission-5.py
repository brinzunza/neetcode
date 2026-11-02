class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            for j in result[:]:
                new = j + [i]
                if new not in result:
                    result.append(new)
        
        return result
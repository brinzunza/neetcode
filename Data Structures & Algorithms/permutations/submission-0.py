class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for i in nums:
            updated = []
            for j in result:
                for k in range(len(j) + 1):
                    copy = j.copy()
                    copy.insert(k, i)
                    updated.append(copy)
            result = updated
        return result
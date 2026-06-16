class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if(seen.get(i, 0) == 0):
                seen[i] = 1
            else:
                return i
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in nums:
            sets += [sub + [num] for sub in sets]

        return sets
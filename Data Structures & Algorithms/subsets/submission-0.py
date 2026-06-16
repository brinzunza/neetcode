class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in nums:
            sets += [subset + [num] for subset in sets]
            print(sets)

        return sets
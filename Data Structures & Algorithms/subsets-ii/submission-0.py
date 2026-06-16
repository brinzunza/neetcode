class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        
        self.backtrack(results, [], nums, 0)
        return results

    def backtrack(self, results, current_subset, nums, start_index):
        results.append(current_subset.copy())
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i-1]:
                continue
            current_subset.append(nums[i])
            self.backtrack(results, current_subset, nums, i + 1)
            current_subset.pop()
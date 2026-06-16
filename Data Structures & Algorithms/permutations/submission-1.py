class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(current):
            if(len(current) == len(nums)):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    backtracking(current)
                    current.pop()
        
        backtracking([])
        return result
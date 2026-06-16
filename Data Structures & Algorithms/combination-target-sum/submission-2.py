class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = {}

        def charCount(state):
            counts = {}

            for char in state:
                counts[char] = counts.get(char, 0) + 1
            
            return tuple(sorted(counts.items()))
        
        def backtracking(state):
            for i in range(len(nums)):
                state.append(nums[i])
                if sum(state) == target:
                    com = charCount(state)
                    if com not in combinations:
                        result.append(state[:])
                        combinations[com] = 1
                    
                elif sum(state) < target:
                    backtracking(state)
                state.pop()



        backtracking([])
        return result


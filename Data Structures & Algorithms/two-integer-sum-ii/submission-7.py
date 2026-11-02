class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        for l in range(len(numbers)):
            s = numbers[l] + numbers[r]
            while(s > target):
                r -= 1
                s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
        
        return

            
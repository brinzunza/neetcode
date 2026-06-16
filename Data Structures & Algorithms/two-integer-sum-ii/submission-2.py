"""
input: int array numbers, int target
output: int array, indices of two numbers that add up to target while not being the same

len of numbers? 0?
size of target? invalid solutions?

pointer at start and end. Check if they add up to target while not being same, if too large, move end down, if too small move start up
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            added = numbers[start] + numbers[end]
            if added == target:
                return [start + 1, end + 1]
            elif added < target:
                start += 1
            else:
                end -= 1
        
        return []

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
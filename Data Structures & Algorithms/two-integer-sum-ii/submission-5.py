"""
input: integer array numbers (empty? size of values? negatives? duplicates?), integer target (always valid solution? negative?)
output: integer array; represents the indices of pairs values in numbers that add up to target

1. for each number, check if sum with every other future number results in target, if so store O(n^2)

2. keep pointer on first index, pointer on last index, if sum is smaller than target move first pointer, if larger, move last pointer, if max, store indices O(n)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while(start < end):
            total = numbers[start] + numbers[end]
            if(total == target):
                return [start + 1, end + 1]
            elif(total < target):
                start += 1
            else:
                end -= 1
        
        return 

"""
test cases: 
1. [1,2] t = 3
2. 
"""
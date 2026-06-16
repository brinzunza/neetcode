'''
Given an array of integers numbers that is sorted in non-decreasing order.
- input array int
- input array is sorted in non-decreasing order

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
- return 2item array int
- pair must add up to target and must be ordered 
- cannot use the same number twice

There will always be exactly one valid solution.
- do not need to check base case

Your solution must use O(1) additional space.
- must be in place 

logic: 
- use two pointers, one at start and one at end
    - if sum of pointers is less than target, move left pointer
    - if sum of pointers is more than target, move right pointer
    - if sum is equal to target, return [left pointer, right pointer]
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while(left < right):
            l = numbers[left]
            r = numbers[right]
            if((l + r) < target):
                left+=1
            elif((l + r) > target):
                right-=1
            else:
                result = [left + 1, right + 1]
                return result
        return
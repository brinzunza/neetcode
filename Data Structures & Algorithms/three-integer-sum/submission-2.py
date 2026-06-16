"""
input: integer array nums (empty? len? values? negatives?)
output: 2d integer array; represents triplets with distinct indices that add up to 0

1. for each number, for each pair, check if third is different and add up to 0 O(n^3)

2. keep pairs in hashtable, iterate through all values and check if sum of pairs and value is 0 O(n^2)

3. sort list, for each value, create two pointers and expand from value depending on sum
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = a + nums[left] + nums[right]
                
                if total == 0:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result


"""
test cases:

1. []
2. [1,2]
3. [1,2,-3]
4. [1,1,2,2,3,3,-6,-7]
5. [-1,0,1,2,-1,-4]
"""
                    
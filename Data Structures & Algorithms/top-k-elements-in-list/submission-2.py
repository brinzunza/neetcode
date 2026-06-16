"""
input: int array nums, int k
output: int array, contains k indices of most frequent elements in array

what is the size of array? empty?
what size values?
what value is k? 0?
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        counts = [[] for _ in range(len(nums) + 1)]
        for num, count in frequencies.items():
            counts[count].append(num)
        
        result = []
        for i in range(len(counts) - 1, 0, -1):
            for num in counts[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
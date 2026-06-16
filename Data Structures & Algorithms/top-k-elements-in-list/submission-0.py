"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
- Input array nums, input int k
- return array of ints

The test cases are generated such that the answer is always unique.
- only one correct answer

You may return the output in any order.
- return array does not need to be in a particular order

Exceptions: 
- how large or small is nums
- how large or small is k

logic:
- Get count of every int in dictionary
- Sort dictionary by key who has most value
- return sub array of first k indices
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            dictionary[i] = dictionary.get(i, 0) + 1
        sorted_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result
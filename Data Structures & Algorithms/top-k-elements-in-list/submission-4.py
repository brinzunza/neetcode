"""
input: integer array nums (empty? negatives? len? always valid answer what is k is larger than distinct values in nums), integer k (0? negatives? larger than length of list?)
output: integer array, represents k most frequent elements in the array

1. for each number, iterate through array to count occurrences and store O(n^2)

2. sort array, iterate through list grouping frequency using window O(nlogn)
 - then place into max heap for easy retrieval

3. for each number, increase count in hashtable, later sort and retrieve k O(nlogn)

4. bucket sort
"""
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        pqueue = []

        start = 0
        end = 0
        while(end < len(nums)):
            while end < len(nums) and nums[start] == nums[end]:
                end += 1
            heapq.heappush(pqueue, (-end + start, nums[start]))
            start = end

        result = []
        for _ in range(min(k, len(pqueue))):
            freq, num = heapq.heappop(pqueue)
            result.append(num)

        return result

"""
test cases
1. [], k = 1
2. [1], k = 1
3. [1,2,2,3,3,3], k = 2
"""
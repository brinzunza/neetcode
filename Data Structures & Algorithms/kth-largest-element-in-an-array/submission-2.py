class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pqueue = nums[:k]
        heapq.heapify(pqueue)

        for num in nums[k:]:
            if num > pqueue[0]:
                heapq.heappop(pqueue)
                heapq.heappush(pqueue, num)

        return pqueue[0]


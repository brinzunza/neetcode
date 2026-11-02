
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.ordered = nums[:]
        heapq.heapify(self.ordered)

        while len(self.ordered) > k:
            heapq.heappop(self.ordered)

    def add(self, val: int) -> int:
        heapq.heappush(self.ordered, val)

        if len(self.ordered) > self.k:
            heapq.heappop(self.ordered)

        return self.ordered[0]

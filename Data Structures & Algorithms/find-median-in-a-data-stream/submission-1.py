class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        left, right = 0, len(self.nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        self.nums.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n == 0:
            return 0
        if n % 2 == 1:
            return self.nums[n // 2]
        return (self.nums[(n // 2) - 1] + self.nums[n // 2]) / 2

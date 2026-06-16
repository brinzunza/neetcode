class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
            
        sums = set()
        sums.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            newSums = set()
            for j in sums:
                if (j + nums[i] == target):
                    return True
                newSums.add(nums[i] + j)
                newSums.add(j)
            sums = newSums
        return False
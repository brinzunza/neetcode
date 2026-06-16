class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for _ in range(len(nums) + 1)]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, occurrences in freq.items():
            counts[occurrences].append(num)

        result = []
        for i in range(len(counts) - 1, -1, -1):
            for num in counts[i]:
                result.append(num)
                if len(result) == k:
                    return result

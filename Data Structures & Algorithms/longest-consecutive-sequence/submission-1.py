class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}

        for num in nums:
            numbers[num] = 1

        result = 0
        for num in nums:
            if numbers.get(num-1, 0) == 0:
                length = 1
                temp = num
                while numbers.get(temp + 1, 0) != 0:
                    length += 1
                    temp += 1
                result = max(result, length)

        return result
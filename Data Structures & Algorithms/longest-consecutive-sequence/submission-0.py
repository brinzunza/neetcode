"""
input: int array nums
output: int array of consecutive numbers

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = num
        
        start = []
        for num in nums:
            if((num - 1) not in map):
                start.append(num)

        sequences = {}
        for num in start:
            i = 1
            sequence = [num]
            while(True):
                if((num + i) in map):
                    sequence.append(num + i)
                    i += 1
                else:
                    break
            sequences[i] = sequence

        max_seq = 0
        for length in sequences.keys():
            if length > max_seq:
                max_seq = length

        return max_seq
        
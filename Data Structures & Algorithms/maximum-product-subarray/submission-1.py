"""
input: integer array nums (values? size? always valid solution? negatives?)
output: integer; represents the largest product possible of a subarray

brute force: compute every subarray and find product, return largest

optimal: dynamic programming
"""

class Solution:
    def maxProduct(self, nums):
        cur_max = cur_min = ans = nums[0]
        for n in nums[1:]:
            cur_max, cur_min = max(n, n*cur_max, n*cur_min), min(n, n*cur_max, n*cur_min)
            ans = max(ans, cur_max)
        return ans

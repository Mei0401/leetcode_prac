#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = nums[0]
        for num in nums:
            if max(curr + num, num) > max_sum:
                curr = max(curr + num, num)
                max_sum = curr
            else:
                if curr + num < 0:
                    curr = 0
                else:
                    curr = curr + num
        return max_sum

#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result


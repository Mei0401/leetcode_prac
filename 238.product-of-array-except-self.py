#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums), [1] * len(nums)
        i = 1
        while i < len(nums):
            left[i] = left[i-1] * nums[i-1]
            right[len(nums)-i-1] = right[len(nums)-i] * nums[len(nums)-i]
            i += 1
        return [left[i]*right[i] for i in range(len(nums))]



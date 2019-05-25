#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2:
            return nums[0]
        curr = nums[0]
        vote = 0
        for i in range(len(nums)):
            if nums[i] == curr:
                vote += 1
            else:
                vote -= 1
                if vote == 0:
                    curr = nums[i]
                    vote = 1
        return curr


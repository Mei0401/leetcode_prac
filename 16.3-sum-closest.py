#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return nums[0]+nums[1]+nums[2]
        nums = sorted(nums)
        best = None
        for curr in range(len(nums)):
            left = curr+1
            right = len(nums)-1
            while left < right:
                curr_get = nums[curr]+nums[left]+nums[right]
                if curr_get == target:
                    return target
                else:
                    if best == None or abs(target - best) > abs(target - curr_get):
                        best = curr_get
                    if target > curr_get:
                        left += 1
                    else:
                        right -= 1
        return best


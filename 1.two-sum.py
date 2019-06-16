#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_dict.keys() and i != nums_dict[target-nums[i]]:
                return [nums_dict[target - nums[i]], i]
            nums_dict[nums[i]] = i
        return []
        


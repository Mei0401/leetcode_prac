#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# low effciency due to modify whole array
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         curr = None
#         i = 0
#         while i < len(nums):
#             if nums[i] != curr:
#                 curr = nums[i]
#                 i += 1
#             else:
#                 nums[i:] = nums[i+1:]
#         return i

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        no_dup = 0
        curr = None
        for i in range(len(nums)):
            if nums[i] != curr:
                curr = nums[i]
                nums[no_dup] = curr 
                no_dup += 1
        nums = nums[:no_dup]
        return no_dup

        


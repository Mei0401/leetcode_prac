#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        curr = len(nums)-1
        while curr >  0:
            if nums[curr-1] < nums[curr]:
                break
            curr -= 1
        if curr == 0:
            nums[:] = nums[::-1]
            return
        curr = len(nums)-1
        prev = curr - 1
        while True:
            if nums[curr] > nums[prev]:
                find = curr
                while find != len(nums):
                    if nums[find] <= nums[prev]:
                        find -= 1
                        break
                    find += 1
                if find == len(nums):
                    find = len(nums)-1
                nums[prev], nums[find] = nums[find], nums[prev]
                nums[curr:] = nums[curr:][::-1]
                break
            curr -= 1
            prev -= 1 
        return
        


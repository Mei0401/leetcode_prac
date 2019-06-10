#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_l = [None] * len(nums)
        for i in range(len(nums)):
            index = nums[i] % len(nums)
            while hash_l[index] != None:
                if hash_l[index] == nums[i]:
                    return True
                else:
                    index = (index+1) % len(nums)
            hash_l[index] = nums[i]
        return False
            

        


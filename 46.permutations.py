#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        if len(nums) == 1:
            return [nums]
        else:
            subs= self.permute(nums[1:])
            result = []
            for sub in subs:
                for pos in range(len(nums)):
                    result.append(sub[:pos]+[nums[0]]+sub[pos:])
            return result
        


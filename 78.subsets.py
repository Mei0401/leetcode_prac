#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        result = [[]]
        for num in nums:
            combination = [curr + [num] for curr in result]
            result += combination
        return result
        


#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {num1:nums1.count(num1) for num1 in nums1}
        result = []
        for num in nums2:
            if num in dict1.keys() and dict1[num] != 0:
                result.append(num)
                dict1[num] -= 1
        return result
        


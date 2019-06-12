#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2)) // 2
        i1 = 0
        i2 = half
        while True:
            left = nums1[:i1] + nums2[:i2]
            right = nums1[i1:] + nums2[i2:]
            if max(left[i1-1], left[-1]) < min(right[0], right[-i2]):
                break
            else:
                left += 1
                right -= 1
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (max(left[i1-1], left[-1]) + min(right[0], right[-i2])) / 2
        else:
            



        


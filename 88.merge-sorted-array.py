#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0: return
        if m==0:
            nums1[:n]=nums2[:]
            return
        nums1[n:m+n] = nums1[:m]
        i1 = n 
        i2 = 0
        for i in range(m+n):
            if i1 == m+n:
                nums1[i:] = nums2[i2:]
                return 
            if i2 == n:
                nums1[i:] = nums1[i1:]
                return
            if nums1[i1] < nums2[i2]:
                nums1[i] = nums1[i1]
                i1 += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
        
        


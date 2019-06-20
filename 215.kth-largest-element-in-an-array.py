#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums == [] or k == 0: return -1
        curr = nums[0]
        large = []
        small = []
        for i in range(1,len(nums)):
            if nums[i] > curr:
                large.append(nums[i])
            elif nums[i] <= curr:
                small.append(nums[i])
        if len(large) == k-1:
            return curr
        else:
            if len(large) > k-1:
                return self.findKthLargest(large, k)
            else:
                return self.findKthLargest(small, k-len(large)-1)


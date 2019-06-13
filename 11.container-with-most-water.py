#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height)-1
        while left != right:
            temp = min(height[left], height[right]) * (right - left)
            if max_water < temp:
                max_water = temp
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1
        return max_water

        


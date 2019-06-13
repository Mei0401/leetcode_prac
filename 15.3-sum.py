#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        n = sorted(nums)
        result = []
        checked = []
        for i in range(len(n)):
            if n[i] not in checked:
                checked.append(n[i])
                need = -1 * n[i]
                left, right  = i+1, len(n)-1
                if left >= right:
                    break 
                while left < right:
                    if need > n[left] + n[right]:
                        left += 1
                    elif need < n[left] + n[right]:
                        right -= 1
                    else:
                        result.append([n[i], n[left], n[right]])
                        while left < right and n[left] == n[left+1]:
                            left += 1
                        while left < right and n[right] == n[right-1]:
                            right -= 1
                        if right - left == 1:
                            break
                        left, right = left+1, right-1
        return result
                


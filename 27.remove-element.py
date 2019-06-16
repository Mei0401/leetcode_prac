#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        if len(nums) == 1: return int(nums[0]!=val)
        curr, tail = 0, len(nums)-1
        while curr <= tail:
            if nums[curr] == val:
                if curr == tail:
                    return curr
                nums[curr], nums[tail] =nums[tail], nums[curr]
                tail -= 1
            else:
                curr += 1
        return curr
        


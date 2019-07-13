#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
def find_bin(nums, target):
    if not nums:
        return -1
    head = 0
    tail = len(nums)-1
    if nums[head] == target:
        return head
    if nums[tail] == target:
        return tail
    if nums[head] > target or nums[tail] < target:
        return -1
    while head <= tail-1:
        mid = (head+tail) // 2
        if mid == head:
            return -1
        elif nums[mid] < target:
            head = mid
        elif nums[mid] > target:
            tail = mid
        elif nums[mid] == target:
            return mid
    return -1

def find_forward(nums):
    # precondtion: nums[0] is the target
    if not nums:
        return 0
    target = nums[0]
    head = 0
    tail = len(nums)-1
    if nums[tail] == target:
        return tail
    while True:
        mid = (head+tail) // 2
        if mid == head:
            return head
        if nums[mid] == target:
            if nums[mid+1] != target:
                return mid
            else:
                head = mid
        else:
            tail = mid




class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = find_bin(nums, target)
        if i == -1:
            return [-1,-1]
        else:
            front_offset = find_forward(nums[:i+1][::-1])
            back_offset = find_forward(nums[i:])
            return [i-front_offset, i+back_offset]

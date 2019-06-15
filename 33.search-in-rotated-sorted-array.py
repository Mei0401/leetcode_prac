#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if nums[0] == target: return 0
        if nums[len(nums)-1] == target: return len(nums)-1
        # conner cases to ensure nums has head and tail to be different
        if nums[0] < nums[-1]:
            head, tail = 0, len(nums)-1
        else:# has been rotated
            tail, head = 0, len(nums)-1
            while head-tail > 1:
                if nums[tail] > nums[(tail+head)//2]:
                    head = (tail+head)//2 
                else: 
                    tail = (tail+head)//2
            if nums[0]<=target<=nums[tail]:
                head, tail = 0, tail
            elif nums[head]<=target<=nums[-1]:
                head, tail = head, len(nums)-1
            else:
                return -1

        #O(logN)
        while head != tail:
            if head >= tail:
                return -1
            else:
                if nums[tail] == target:
                    return tail
                elif nums[head] == target:
                    return head
                elif (head+tail)//2 == head:
                    return -1
                elif nums[(head+tail)//2] == target:
                    return (head+tail)//2
                elif nums[(head+tail)//2] > target:
                    tail = (head+tail)//2
                else:
                    head = (head+tail)//2
        return -1
        


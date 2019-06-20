#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# merge sort
def mergeList(start, right_start):
        if start == None:
            return right_start
        
        if right_start == None:
            return start
        
        if start.val < right_start.val:
            result = start
            result.next = mergeList(start.next, right_start)
        else:
            result = right_start
            result.next = mergeList(start, right_start.next)
        return result

class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        elif not head.next.next:
            if head.val > head.next.val:
                temp = head.next
                head.next.next = head
                head.next = None
                return temp
            return head
        else:
            half, curr = head,head
            while curr != None and curr.next != None:
                half = half.next
                curr = curr.next.next 
            R = half.next
            half.next = None
            L, R = self.sortList(head), self.sortList(R)
            
            return mergeList(L, R)

        


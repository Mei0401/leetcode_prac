#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        while n > 0:
            curr = curr.next
            n -= 1
        if curr == None:
            head = head.next
            return head
        tail = curr
        curr = head
        while tail.next:
            tail = tail.next
            curr = curr.next 
        curr.next = curr.next.next
        return head
        


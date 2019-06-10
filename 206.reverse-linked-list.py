#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
     def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if head.next == None:
            return head
        rev = self.reverseList(head.next)
        curr = rev
        while curr.next:
            curr = curr.next
        head.next = None
        curr.next = head
        return rev

        


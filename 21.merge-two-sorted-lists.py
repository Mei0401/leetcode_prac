#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # head = l1
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if l1.val>l2.val:
        #     head = l2
        #     l2 = l2.next
        # else:
        #     l1 = l1.next 
        # curr = ListNode(head.val)
        # head = curr
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         curr.next = ListNode(l1.val)
        #         l1 = l1.next 
        #     else:
        #         curr.next = ListNode(l2.val)
        #         l2 = l2.next
        #     curr = curr.next 
        # if not l1:
        #     curr.next = l2
        # if not l2:
        #     curr.next = l1
        # return head
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2


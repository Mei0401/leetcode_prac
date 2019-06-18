#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0 or head.next == None: return head 
        
        new_tail = length - k
        curr = head
        while new_tail > 1:
            curr = curr.next
            new_tail -= 1
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head



        


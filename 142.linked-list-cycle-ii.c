/*
 * @lc app=leetcode id=142 lang=c
 *
 * [142] Linked List Cycle II
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    if(head == NULL || head->next == NULL){
        return NULL;
    }
    struct ListNode *ptr1 = head;
    struct ListNode *ptr2 = head;
    while(true){
        ptr1 = ptr1->next;
        if(ptr2->next == NULL || ptr2->next->next == NULL){
            return NULL;
        }
        ptr2 = ptr2->next->next;
        if(ptr1 == ptr2){
            break;
        }
    }
    ptr1 = head;
    while(ptr1 != ptr2){
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    return ptr1; 
}


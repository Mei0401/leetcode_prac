/*
 * @lc app=leetcode id=141 lang=c
 *
 * [141] Linked List Cycle
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if(!head){
        return false;
    }
    int step = 0;
    struct ListNode *ptr_1 = head;
    struct ListNode *ptr_2 = head;
    while(ptr_1->next){
        if(step != 0){
            ptr_2 = ptr_2->next;
            step = 0;
        }else{
            step = 1;
        }
        ptr_1 = ptr_1->next;
        if(ptr_1->val == ptr_2->val){
            return true;
        }
    }
    return false;
}


/*
 * @lc app=leetcode id=160 lang=c
 *
 * [160] Intersection of Two Linked Lists
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    if (headA == NULL || headB == NULL)
    {
        return NULL;
    }
    struct ListNode *path_1 = headA;
    struct ListNode *path_2 = headB;
    int flag_1 = 0;
    int flag_2 = 0;
    while (flag_1 != 2 && flag_2 != 2)
    {
        if (path_1 == path_2)
        {
            return path_1;
        }
        else
        {
            if (!path_1->next)
            {
                path_1 = headB;
                flag_1 += 1;
            }
            else
            {
                path_1 = path_1->next;
            }
            if (!path_2->next)
            {
                path_2 = headA;
                flag_2 += 1;
            }
            else
            {
                path_2 = path_2->next;
            }
        }
    }
    return NULL;
}

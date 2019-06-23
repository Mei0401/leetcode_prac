#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def find_path(curr, target):
    if curr == target:
        return [curr]
    elif curr == None:
        return []
    else:
        l = find_path(curr.left, target)
        r = find_path(curr.right, target)
        if l != []:
            return [curr] + l
        elif r != []:
            return [curr] + r
        else:
            return [] 


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = find_path(root, p)
        q_path = find_path(root, q)
        i = 0
        result = p_path[0]
        while i < len(p_path) and i < len(q_path):
            if p_path[i].val == q_path[i].val:
                result = p_path[i]
            else:
                break
            i += 1
        return result
        


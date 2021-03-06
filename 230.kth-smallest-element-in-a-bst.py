#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def get_inorder(root):
    if not root:
        return []
    return get_inorder(root.left) + [root.val] + get_inorder(root.right)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return get_inorder(root)[k-1]
            
        


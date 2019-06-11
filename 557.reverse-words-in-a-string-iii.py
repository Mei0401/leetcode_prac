#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        stack = []
        s = s+" "
        for i in range(len(s)):
            if s[i].isspace():
                while stack != []:
                    rev += stack.pop()
                rev += " "
            else:
                stack.append(s[i])
        return rev[:-1]


#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(0)
            elif c == '[':
                stack.append(1)
            elif c == '{':
                stack.append(2)
            elif len(stack) == 0:
                return False
            elif c == ')':
                if stack[-1] == 0:
                    stack.pop()
                else:
                    return False 
            elif c == ']':
                if stack[-1] == 1:
                    stack.pop()
                else:
                    return False 
            elif c == '}':
                if stack[-1] == 2:
                    stack.pop()
                else:
                    return False 
        return len(stack) == 0
        


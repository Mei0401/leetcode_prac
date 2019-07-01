#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        postive = False
        if min(divisor,dividend,0) == 0:
            postive = True
        else:
            if divisor < 0 and dividend <0:
                postive = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend == divisor:
            if postive:
                return 1
            else:
                return -1
        elif dividend < divisor:
            return 0
        elif dividend < divisor + divisor:
            if postive:
                return 1
            else:
                return -1
        result = 0
        curr_divisor = divisor
        curr_i = 1
        while curr_divisor < dividend:
            dividend -= curr_divisor
            result += curr_i
            curr_divisor += curr_divisor
            curr_i += curr_i
        result = result + self.divide(dividend, divisor)
        if postive:
            return min(2**31-1,result)
        else:
            return max(-2**31, 0-result)
        
        
        


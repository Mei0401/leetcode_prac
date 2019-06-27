#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        str_x = str(x)
        if x < 0:
            str_x= str_x[1:]
        for i in range(len(str_x)):
            result += int(str_x[i])*(10**(i))
        if result > 2**31:
            return 0
        if x<0:      
            result *= -1
        return result
        


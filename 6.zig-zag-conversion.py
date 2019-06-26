#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        result = ["" * 1 for _ in range(numRows)]
        d_x, d_x = 0,1
        x,y = 0,0
        for c in s:
            result[y] += c
            if y == numRows-1:
                d_x, d_y = 1, -1
            elif y == 0:
                d_x, d_y = 0,1
            x += d_x
            y += d_y
        
        return "".join(result)
            

        


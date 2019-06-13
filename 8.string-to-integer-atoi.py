#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
class Solution:
    def myAtoi(self, str: str) -> int:
        result = 0
        sign = 0
        for i in range(len(str)):
            if str[i].isspace() and sign == 0:
                continue
            elif str[i] == '-' and sign == 0:
                sign = -1
            elif str[i] == '+' and sign == 0:
                sign = 1
            elif str[i].isnumeric():
                if sign == 0:
                    sign = 1
                result = 10*result + ord(str[i]) - ord('0')
                if result > 2147483647 and sign == 1:
                    return 2147483647
                if result > 2147483648 and sign == -1:
                    return -2147483648
            else:
                return sign * result
        return sign * result
        


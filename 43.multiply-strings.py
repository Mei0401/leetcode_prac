#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1)>len(num2):
            num1,num2 = num2,num1
        if num1[0] == 0 or num2[0] == 0:
            return "0"
        temp = 0
        for i in range(len(num1)):
            temp += (ord(num1[len(num1) - i - 1]) - ord('0')) * (10**i)
        dict_num1 = [0]*10
        for i in range(10):
            dict_num1[i] = i * temp
        temp = 0
        for i in range(len(num2)):
            temp += dict_num1[ord(num2[len(num2) - i - 1]) - ord('0')] * (10**i)
        return str(temp)
        
        

        


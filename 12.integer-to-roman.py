#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ""
        elif num >= 1000:
            return "M"*(num//1000) + self.intToRoman(num%1000)
        elif num >= 900:
            return "CM" + self.intToRoman(num-900)
        elif num >= 500:
            return "D"*(num//500) + self.intToRoman(num%500)
        elif num >= 400:
            return "CD" + self.intToRoman(num-400)
        elif num >= 100:
            return "C"*(num//100) + self.intToRoman(num%100)
        elif num >= 90:
            return "XC" + self.intToRoman(num-90)
        elif num >= 50:
            return "L"*(num//50) + self.intToRoman(num%50)
        elif num >= 40:
            return "XL" + self.intToRoman(num-40)
        elif num >= 10:
            return "X"*(num//10) + self.intToRoman(num%10)
        elif num >= 9:
            return "IX" + self.intToRoman(num-9)
        elif num >= 5:
            return "V"*(num//5) + self.intToRoman(num%5)
        elif num >= 4:
            return "IV" + self.intToRoman(num-4)
        elif num >= 1:
            return "I"*(num)


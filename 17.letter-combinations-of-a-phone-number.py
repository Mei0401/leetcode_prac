#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

d = {
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits.isdigit():
            return []
        result = [""]
        while len(digits) > 0:
            curr = digits[-1]
            temp = []
            for curr_l in d[curr]:
                for result_l in result:
                    temp.append(curr_l+result_l)
            result = temp
            digits = digits[:-1]
        return result
            
        


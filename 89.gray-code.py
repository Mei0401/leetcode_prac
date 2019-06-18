#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
class Solution:
    def grayCode(self, n: int) -> List[int]:
        r = [0]
        for i in range(n):
            # x or 1<<i => sign i bit in x to 1
            r.extend([x | 1<<i for x in r[::-1]])
        return r

        


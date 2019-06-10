#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 : return False
        if n & n-1 == 0:
            return True
        return False


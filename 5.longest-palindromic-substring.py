#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    # need looking for Manacher algorithm
    def longestPalindrome(self, s: str) -> str:
        # define: for dp(i,j) => return if s[i,j] is palindromic
        # dp(i,j) => dp(i+1,j-1) and s[i]==s[j]
        dp = []
        for start in range(len(s)):
            dp.append([False] * len(s))
        max_length = 1
        result = [0,1]
        for start in range(0,len(s)):
            dp[start][start] = True
        for end in range(1,len(s)):
            for start in range(end-1,-1,-1):
                if max_length == len(s):
                    break
                dp[start][end] = (dp[start+1][end-1] or end-start == 1) and s[start] == s[end]
                if max_length < end-start+1 and dp[start][end]:
                    max_length = end-start+1
                    result = [start,end+1]
        return s[result[0]:result[1]]




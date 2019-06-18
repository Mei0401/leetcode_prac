#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0] = [1 for i in range(n)]
        for i in range(m):
            dp[i][0] = 1
        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]
        


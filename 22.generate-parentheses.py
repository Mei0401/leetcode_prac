#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        dp = [[""],["()"]]
        for i in range(2,n+1):
            temp = []
            # (sub) rest = result
            for sub in range(i):
                rest = i - sub - 1
                for sub_p in dp[sub]:
                    for rest_p in dp[rest]:
                        temp.append("("+sub_p+")"+rest_p)
            dp.append(temp)
        return dp[-1]


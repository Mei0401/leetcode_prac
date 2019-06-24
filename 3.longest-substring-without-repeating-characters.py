#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start, end = 0, 1
        max_len = 1
        while end < len(s):
            curr = s[start:end]
            if s[end] not in curr:
                end += 1
                if end - start > max_len:
                    max_len = end - start
            else:
                while s[end] in s[start:end]:
                    start += 1
        return max_len



#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
def flip(matrix):
    for y in range(len(matrix)):
        for x in range(y, len(matrix)):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flip(matrix)
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        


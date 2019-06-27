#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
def check_repeat(l):
    l = list(filter(lambda num:num != '.', l))
    for num in l:
        if l.count(num) > 1:
            return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        topL, topR= 0,2,0,2
        for i in range(9):
            if not (check_repeat(board[i]) and check_repeat([board[y][i] for y in range(9)])):
                return False
            square = []
            for y in range(topL, bottomL+1):
                for 
            
        


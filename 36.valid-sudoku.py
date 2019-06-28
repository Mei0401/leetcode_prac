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
        topX, topY= 0,0
        for i in range(9):
            if not (check_repeat(board[i]) and check_repeat([board[y][i] for y in range(9)])):
                return False
            square = []
            for dx in range(3):
                for dy in range(3):
                    square.append(board[topY+dy][topX+dx])
            if not check_repeat(square):
                return False
            topX += 3
            if topX == 9:
                topX = 0
                topY += 3
        return True
            
        


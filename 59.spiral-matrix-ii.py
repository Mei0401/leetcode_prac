#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0: return []
        direction = 0 # 0 right, 1 down, 2 left, 3 up
        result = [[-1] * n for _ in range(n)]
        pos = [0,0]
        curr = 1
        while n > 0:
            if direction == 0:
                for i in range(n):
                    result[pos[0]][pos[1]+i] = curr+i
                pos = [pos[0]+1,pos[1]+n-1]
                curr += n
                direction = 1
                n -= 1
            elif direction == 1:
                for i in range(n):
                    result[pos[0]+i][pos[1]] = curr+i
                pos = [pos[0]+n-1,pos[1]-1]
                curr += n
                direction = 2
            elif direction == 2:
                for i in range(n):
                    result[pos[0]][pos[1]-i] = curr+i
                pos = [pos[0]-1,pos[1]-n+1]
                curr += n
                direction = 3
                n-=1
            elif direction == 3:
                for i in range(n):
                    result[pos[0]-i][pos[1]] = curr+i
                pos = [pos[0]-n+1,pos[1]+1]
                curr += n
                direction = 0
        return result

            




        


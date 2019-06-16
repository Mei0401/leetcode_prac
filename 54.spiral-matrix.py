#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        elif len(matrix) == 1:
            return matrix[0]
        elif len(matrix) == 2:
            return matrix[0] + matrix[1][::-1]
        elif len(matrix[0]) == 1:
            result = []
            for i in range(len(matrix)):
                result.extend(matrix[i])
            return result
        elif len(matrix[0]) == 2:
            result = matrix[0]
            for i in range(1, len(matrix)):
                result.append(matrix[i][1])
            for i in range(1, len(matrix)):
                result.append(matrix[-i][0])
            return result
        else:
            sub = matrix[1:-1]
            for i in range(len(sub)):
                sub[i] = sub[i][1:-1]
            sub = self.spiralOrder(sub)
            result = matrix[0]
            for i in range(1, len(matrix)-1):
                result.append(matrix[i][-1])
            result.extend(matrix[-1][::-1])
            for i in range(2, len(matrix)):
                result.append(matrix[-i][0])
            return result + sub





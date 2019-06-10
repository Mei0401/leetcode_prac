#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minusMin = []
        self.min = None
        

    def push(self, x: int) -> None:
        if self.min == None:
            self.min = x
            self.minusMin.append(0)
        else:
            if x - self.min < 0:
                self.minusMin.append(x - self.min)
                self.min = x
            else:
                self.minusMin.append(x - self.min)


    def pop(self) -> None:
        if self.minusMin[-1] >= 0:
            pass
            # t = self.minusMin[-1] + self.min
        else:
            # t = self.min
            self.min = self.min - self.minusMin[-1]
        self.minusMin = self.minusMin[:-1]       

    def top(self) -> int:
        if self.minusMin[-1] > 0:
            t = self.minusMin[-1] + self.min
        else:
            t = self.min
        return t
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


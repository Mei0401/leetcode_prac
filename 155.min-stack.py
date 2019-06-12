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
        self.minList = []
        self.elements = []
        

    def push(self, x: int) -> None:
        if not self.elements:
            self.minList.append(x)
        else:
            if x < self.minList[-1]:
                self.minList.append(x)
            else:
                self.minList.append(self.minList[-1])
        self.elements.append(x)


    def pop(self) -> None:
        self.elements.pop()
        self.minList.pop()       

    def top(self) -> int:
        return self.elements[-1]
        

    def getMin(self) -> int:
        return self.minList[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


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
        self.body = []
        self.sort = []

    def push(self, x: int) -> None:
        self.body.append(x)
        if not self.sort:
            self.sort.append(x)
        else:
            for i in range(len(self.sort)):
                if self.sort[i] > x:
                    self.sort = self.sort[:i+1] + x + self.sort[i+1:]
                    return
            self.sort.append(x)

    def pop(self) -> None:
        if self.body:
            if not self.body[:-1]:
                self.body = []
            if self.body[-1] == self.min:
                new_min = self.body[0]
                for num in self.body[:-1]:
                    if new_min > num:
                        new_min = num 
                self.min = new_min
            self.body = self.body[:-1]
        

    def top(self) -> int:
        if self.body:
            return self.body[-1]
        return

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


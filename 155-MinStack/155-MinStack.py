# Last updated: 13.08.2025, 16:59:09
class MinStack:

    def __init__(self):
        self.min_lst = []
        self.lst = []

    def push(self, val: int) -> None:

        if not self.min_lst or val < self.min_lst[-1]:
            self.min_lst.append(val)
        else:
            self.min_lst.append(self.min_lst[-1])

        self.lst.append(val)
        

    def pop(self) -> None:
        self.lst.pop()
        self.min_lst.pop()
        

    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
        return self.min_lst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
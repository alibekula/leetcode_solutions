# Last updated: 27.09.2025, 06:25:53
class MinStack:
# 1, 2, 2, 2, -5, 8,  1
# 1, 1, 1, 1, -5, -5, -5
    def __init__(self):
        self.min_stack = []
        self.stack = []
        self.curr_min = None
    def push(self, val: int) -> None:

        if self.curr_min is None:
            self.curr_min = val
        elif val < self.curr_min:
            self.curr_min = val
        
        self.stack.append(val)
        self.min_stack.append(self.curr_min)
        

    def pop(self) -> None:
        self.stack.pop()
        minimum = self.min_stack.pop()
        if self.curr_min == minimum:
            self.curr_min = self.min_stack[-1] if self.min_stack else None 


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
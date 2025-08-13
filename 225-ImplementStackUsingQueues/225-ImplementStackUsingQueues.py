# Last updated: 13.08.2025, 16:58:28

class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        val = self.stack.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
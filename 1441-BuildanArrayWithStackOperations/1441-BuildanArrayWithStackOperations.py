# Last updated: 22.11.2025, 21:36:35
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        stack = []

        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                res = ops[t](a, b)
                stack.append(res)
            else:
                stack.append(int(t))
        
        return stack.pop()

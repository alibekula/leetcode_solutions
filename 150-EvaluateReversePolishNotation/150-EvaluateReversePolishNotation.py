# Last updated: 13.08.2025, 16:59:13
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dct = {'+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: int(x/y)}
        
        stack = []

        for token in tokens:
            if token not in dct:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(dct[token](x, y))
        
        return stack[0]
        
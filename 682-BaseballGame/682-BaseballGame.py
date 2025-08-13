# Last updated: 13.08.2025, 16:57:02
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [0]

        for oper in operations:

            if oper.isdigit() or oper[1:].isdigit():
                stack.append(int(oper))
            elif oper == 'C':
                stack.pop()
            elif oper == 'D':
                stack.append(stack[-1]*2)
            elif oper == '+':
                stack.append(stack[-1] + stack[-2])
            print(stack)
        return sum(stack) 

                

        
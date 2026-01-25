# Last updated: 26.01.2026, 02:51:14
1class Solution:
2    def makeGood(self, s: str) -> str:
3        
4        stack = []
5        big = set(chr(i) for i in range(ord('Z'), ord('A')-1, -1))
6        small = set(chr(i) for i in range(ord('z'), ord('a')-1, -1))
7
8        def check(a, b):
9            if a.lower() == b.lower() and ((a in big and b in small) or (a in small and b in big)):
10                return True
11            
12            return False
13
14
15        for char in s:
16
17            if stack and check(stack[-1], char):
18                stack.pop()
19            else:
20                stack.append(char)
21        
22        return ''.join(stack)
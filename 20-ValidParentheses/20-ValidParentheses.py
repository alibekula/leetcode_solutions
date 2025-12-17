# Last updated: 17.12.2025, 19:28:21
1class Solution:
2    def isValid(self, s: str) -> bool:
3        
4        dct = {'(': ')',
5                '{': '}',
6                '[': ']'}
7
8        stack = []
9
10        for char in s:
11            if char in dct:
12                stack.append(char)
13            else:
14                if stack and dct[stack[-1]] == char:
15                    stack.pop()
16                else:
17                    return False
18        
19        return True if not stack else False
# Last updated: 15.12.2025, 21:44:36
1class Solution:
2    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
3        visited = set()
4        n = len(values)
5        total = 0
6        i = 0
7
8        while True:
9
10            if not (0 <= i < n):
11                return total
12            
13            if i in visited:
14                return total
15
16            visited.add(i)
17            
18            if instructions[i] == 'add':
19                total += values[i]
20                i += 1
21            else:
22                i = values[i] + i
23                
24            
25                
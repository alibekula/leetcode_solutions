# Last updated: 16.12.2025, 21:19:11
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        ans = []
4
5        def dfs(l=0, r=0, s=''):
6            nonlocal n
7            if len(s) == n * 2:
8                ans.append(s)
9                return 
10            
11            if l < n:
12                dfs(l+1, r, s+'(')
13            
14            if r < l:
15                dfs(l, r+1, s+')')
16        
17        dfs()
18
19        return ans
20
21
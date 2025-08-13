# Last updated: 13.08.2025, 16:58:35
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        used = set()
        res = []

        def dfs(curr, s, i):
            if curr > n:
                return

            if curr == n and len(s) == k:
                res.append(s[::])
                return
            
            for j in range(i, 10):

                if j not in used:   
                    used.add(j)
                    s.append(j)
                    dfs(curr+j, s, j+1)
                
                    used.remove(j)
                    s.pop()
            
        dfs(0, [], 1)
        return res
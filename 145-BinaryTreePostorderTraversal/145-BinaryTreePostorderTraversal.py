# Last updated: 08.09.2025, 20:19:46
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        n, m = len(heights), len(heights[0])

        def dfs(i, j, reachable):
            nonlocal n, m
            reachable.add((i, j))
            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for x, y in directions:
                di = i + x
                dj = j + y

                if (di, dj) in reachable or not (0<=di<n and 0<=dj<m):
                    continue
                
                if heights[i][j] > heights[di][dj]:
                    continue

                dfs(di, dj, reachable)
        
        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m-1, atlantic)
        
        for j in range(m):
            dfs(0, j, pacific)
            dfs(n-1, j, atlantic)
        
        return list(pacific.intersection(atlantic))
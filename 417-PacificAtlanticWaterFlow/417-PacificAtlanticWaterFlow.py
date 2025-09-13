# Last updated: 13.09.2025, 15:14:17
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: 
            return []
        
        n, m = len(heights), len(heights[0])
        
        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                i, j = q.popleft()
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                        if heights[ni][nj] >= heights[i][j]:
                            visited.add((ni, nj))
                            q.append((ni, nj))
            return visited
        
        pacific_starts = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]
        atlantic_starts = [(n-1, j) for j in range(m)] + [(i, m-1) for i in range(n)]
        
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        
        return list(map(list, pacific & atlantic))

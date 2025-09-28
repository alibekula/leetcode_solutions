# Last updated: 28.09.2025, 10:23:20
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def search(i, j):
            nonlocal n, m
            if not (0 <= i < n and 0 <= j < m) or grid[i][j] == '0':
                return 
            
            grid[i][j] = '0'

            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for x, y in directions:
                search(i+x, j +y)
        
        n, m = len(grid), len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    search(i, j)
        
        return count 

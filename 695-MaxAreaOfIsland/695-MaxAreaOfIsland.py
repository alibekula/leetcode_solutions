# Last updated: 13.09.2025, 15:13:58
class Solution:

    def sink(self, i, j, count=0):
        if (not ((0 <= i < self.n) and (0 <= j < self.m))) or (self.grid[i][j] == 0):
            return 0
        
        self.grid[i][j] = 0
        count = 1
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for dx, dy in directions:
            count += self.sink(i + dx, j + dy, count)
        
        return count


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.n, self.m = len(grid), len(grid[0])
        self.grid = grid
        max_count = 0

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 1:
                    max_count = max(self.sink(i, j), max_count)
        
        return max_count
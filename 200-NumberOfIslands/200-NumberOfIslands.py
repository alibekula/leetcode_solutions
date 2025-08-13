# Last updated: 13.08.2025, 16:58:52
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        if not grid or not grid[0]:
            return 0
        
        def dfs(row, col):
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0 or grid[row][col] == "0":
                return
                
            grid[row][col] = '0'

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
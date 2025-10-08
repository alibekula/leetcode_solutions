# Last updated: 08.10.2025, 19:09:49
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])

        if n==0 or m == 0:
            return 0
        
        i, j = n-1, 0
        count = 0

        while i >= 0 and j < m:
            if grid[i][j] < 0:
                count += m - j
                i -= 1
            elif grid[i][j] >= 0:
                j += 1
        
        return count
            
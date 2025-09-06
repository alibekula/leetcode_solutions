# Last updated: 06.09.2025, 21:51:04
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top, down, left, right = float('inf'), float('-inf'), float('inf'), float('-inf')

        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    top = min(top, i+1)
                    down = max(down, i+1)
                    left = min(left, j+1)
                    right = max(right, j+1)

        ans = (right-left +1) * (down - top+1)

        return ans if ans != float('inf') else 0  
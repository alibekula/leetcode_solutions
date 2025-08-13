# Last updated: 13.08.2025, 16:56:17
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[None] * (n + 2)] + [[None] + [1] * n + [None] for _ in range(m)] + [[None] * (n + 2)]

        for i, j in walls:
            grid[i + 1][j + 1] = 'Wall'
        for i, j in guards:
            grid[i + 1][j + 1] = 'Guard'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        for i, j in guards:
            i, j = i + 1, j + 1  
            for di, dj in directions:
                x, y = i + di, j + dj
                while grid[x][y] == 1 or grid[x][y] == 'Guarded':  
                    grid[x][y] = 'Guarded'
                    x, y = x + di, y + dj

        count = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i][j] == 1:  
                    count += 1

        return count

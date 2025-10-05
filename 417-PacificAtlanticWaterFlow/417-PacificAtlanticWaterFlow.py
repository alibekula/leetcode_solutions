# Last updated: 05.10.2025, 10:52:19
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        h = heights
        n, m = len(h), len(h[0])

        pac, atl = deque(), deque()

        for j in range(m):
            pac.append((0, j))
            atl.append((n - 1, j))
        
        for i in range(n):
            pac.append((i, 0))
            atl.append((i, m - 1))

        dct = {'pacific': set(), 'atlantic' : set()}
        for ocean, name in [(pac, 'pacific'), (atl, 'atlantic')]:
            while ocean:
                x, y = ocean.popleft()
                d = [(0,1), (1,0), (-1,0), (0,-1)]

                if (x, y) in dct[name]:
                    continue
                dct[name].add((x, y))

                for dx, dy in d:
                    if 0 <= dx + x < n and 0 <= dy + y < m and h[x][y] <= h[dx+x][dy+ y]:
                        ocean.append((dx+x, dy+y))

            
        return list(dct['pacific'].intersection(dct['atlantic']))
                    




# Last updated: 03.10.2025, 12:11:17
import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        n, m = len(heightMap), len(heightMap[0])

        if n == 0 or m == 0:
            return 0
        
        heap = []
        visited = [[False] * m for i in range(n)]

        for i in range(n):
            for j in (0, m-1):
                visited[i][j] = True
                heapq.heappush(heap, [heightMap[i][j], i, j])
        
        
        for j in range(m):
            for i in (0, n-1):
                visited[i][j] = True
                heapq.heappush(heap, [heightMap[i][j], i, j])
        
        ans = 0

        while heap:

            h, i, j = heapq.heappop(heap)

            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for dx, dy in directions:
                new_i, new_j = dx + i, dy + j
                if (new_i >= 0 and  new_i < n) and (new_j >= 0 and new_j < m) and visited[new_i][new_j] is not True:
                    visited[new_i][new_j] = True
                    nei_h = heightMap[new_i][new_j]

                    if h >= nei_h:
                        ans += h - nei_h
                        heapq.heappush(heap, [h, new_i, new_j])

                    else:
                        heapq.heappush(heap, [nei_h, new_i, new_j])
        
        return ans
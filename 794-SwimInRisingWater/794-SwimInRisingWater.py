# Last updated: 12.09.2025, 03:07:18
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        heap = []
        max_cost = grid[n-1][m-1]

        heapq.heappush(heap, [grid[n-1][m-1], n-1, m-1])
        visited = set()
        while heap:
            cost, i, j = heapq.heappop(heap)
            max_cost = max(max_cost, cost)

            if (i, j) == (0, 0):
                return max_cost
            
            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for x, y in directions:
                xi, yj = i+x, j+y
                if (0<=xi<n and 0<=yj<m) and (xi, yj) not in visited:
                    visited.add((xi, yj))
                    new_cost = max(grid[xi][yj], max_cost)
                    heapq.heappush(heap, [new_cost, xi, yj])



# Last updated: 13.08.2025, 18:46:43
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = sorted(zip(capital, profits))
        idx = 0
        heap = []
        n = len(capital)

        for _ in range(k):

            while idx < n and projects[idx][0] <= w:
                heapq.heappush(heap, -projects[idx][1])
                idx += 1
            
            if not heap:
                return w
            
            w -= heapq.heappop(heap)
        
        return w
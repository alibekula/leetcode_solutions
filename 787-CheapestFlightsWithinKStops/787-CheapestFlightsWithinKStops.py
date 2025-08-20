# Last updated: 21.08.2025, 01:23:42
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for start, end, price in flights:
            graph[start].append([end, price])
        
        heap = []
        prices = dict()
        heapq.heappush(heap, [0, src, 0])

        while heap:
            curr, node, stops = heapq.heappop(heap)

            if stops > k+1:
                continue
            
            if node == dst:
                return curr
            
            if curr < prices.get((node, stops+1), float('inf')):
                prices[(node,stops+1)] = curr
            
                for nei, w in graph[node]:
                    heapq.heappush(heap, [curr+w, nei, stops+1])
        
        return -1
        
            
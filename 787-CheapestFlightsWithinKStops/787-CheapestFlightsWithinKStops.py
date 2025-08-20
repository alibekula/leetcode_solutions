# Last updated: 21.08.2025, 01:32:41
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for start, end, price in flights:
            graph[start].append([end, price])
        
        heap = []
        flights_count = {}
        heapq.heappush(heap, [0, src, 0])

        while heap:
            curr, node, stops = heapq.heappop(heap)

            if node in flights_count and flights_count[node] <= stops:
                continue
            
            flights_count[node] = stops

            if node == dst:
                return curr
            
            if stops <= k:
                for nei, w in graph[node]:
                    heapq.heappush(heap, [curr+w, nei, stops+1])
        
        return -1
        
            
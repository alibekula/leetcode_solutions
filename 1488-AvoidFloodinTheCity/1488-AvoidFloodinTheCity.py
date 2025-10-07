# Last updated: 07.10.2025, 18:56:26
from collections import deque
import heapq
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        n = len(rains)
        ans = [-1] * n
        future = dict()
        heap = []

        for day, lake in enumerate(rains):
            if lake not in future:
                future[lake] = deque([])
            
            future[lake].append(day)

        seen = set()
        for day, lake in enumerate(rains):
            
            if lake != 0:
                if lake in seen:
                    return []
                
                seen.add(lake)
                future[lake].popleft()

                if not future[lake]:
                    del future[lake]
                else:
                    heapq.heappush(heap, [future[lake][0], lake])
                ans[day] = -1
            
            else:
                if heap:
                    _, lake = heappop(heap)
                    ans[day] = lake
                    seen.remove(lake)
                else:
                    ans[day] = 1
        
        return ans



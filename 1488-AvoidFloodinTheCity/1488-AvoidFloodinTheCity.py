# Last updated: 07.10.2025, 18:42:42
from collections import deque
import heapq
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        ans = []
        zeros = []
        count = {}

        for day, lake in enumerate(rains):

            if lake not in count:
                if lake == 0:
                    zeros.append(day)
                    ans.append(-1)
                    continue
                count[lake] = day
            else:
                if not zeros:
                    return []
                else:
                    first_day = count[lake]
                    last_day = day
                    count[lake] = last_day
                    pos = None

                    for idx,zero_day in enumerate(zeros):
                        if zero_day > first_day:
                            pos = zero_day
                            zeros.pop(idx)
                            break

                    if pos is None:
                        return []

                    ans[pos] = lake


            ans.append(-1)
        
        for i in range(1, 10**9+1):
            if i not in count:
                new_lake = i
                break
        heap = []
        for lake, day in count.items():
            heapq.heappush(heap, [day, lake])
        
        while zeros and heap and zeros[0] > heap[0][0]:
            pos = zeros.pop()
            _, lake = heapq.heappop(heap)
            ans[pos] = lake
        
        while zeros:
            pos = zeros.pop()
            ans[pos] = new_lake
        
        return ans
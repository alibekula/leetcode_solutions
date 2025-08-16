# Last updated: 16.08.2025, 17:35:25
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {key: [] for key in range(1, n+1)}

        for u, v, m in times:
            graph[u].append([m, v])

        heap = []

        min_path = 0
        distances = [float('inf') if i != k else 0 for i in range(1, n+1)]
        heapq.heappush(heap, [0, k])

        while heap:
            curr_weight, curr_node = heapq.heappop(heap)

            if distances[curr_node-1] < curr_weight:
                continue

            for weight, node in graph[curr_node]:
                new_dist = weight + curr_weight
                if new_dist < distances[node-1]:
                    distances[node-1] = new_dist
                    heapq.heappush(heap, [new_dist, node])
        
        ans = max(distances)

        return ans if ans != float('inf') else -1 
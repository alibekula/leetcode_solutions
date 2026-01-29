# Last updated: 29.01.2026, 07:43:28
1class Solution:
2    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
3        
4        graph = defaultdict(list)
5        min_dist = {(i, i): 0 for i in original}
6
7        for u, v, w in zip(original, changed, cost):
8            graph[u].append([v, w])
9        
10        total = 0
11
12        def get_path(left, right):
13            if (left, right) in min_dist:
14                return min_dist[(left, right)]
15            
16            heap = [[0, left]]
17
18            while heap:
19                score, node = heapq.heappop(heap)
20
21                if node == right:
22                    if (left, right) not in min_dist or min_dist[(left, right)] > score:
23                        min_dist[(left, right)] = score
24                        return score 
25
26                for nei, wei in graph[node]:
27
28                    if (left, nei) not in min_dist or min_dist[(left, nei)] > score+wei:
29                        min_dist[(left, nei)] = score + wei
30                        heapq.heappush(heap, [score+wei, nei])
31            
32            return min_dist[(left, right)] if (left, right ) in min_dist else float('inf')
33                    
34
35
36        for l, r in zip(source, target):
37            if l != r:
38                price = get_path(l, r)
39                if price == float('inf'):
40                    return -1
41                
42                total += price
43        
44        return total
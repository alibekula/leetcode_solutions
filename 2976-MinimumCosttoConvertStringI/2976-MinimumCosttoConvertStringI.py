# Last updated: 29.01.2026, 07:55:48
1class Solution:
2    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
3        
4        graph = defaultdict(list)
5        min_dist = {(chr(i), chr(i)): 0 for i in range(ord('a'), ord('z')+1)}
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
32            if (left, right) not in min_dist:
33                min_dist[(left, right)] = float('inf')
34
35        for char1 in ''.join(chr(i) for i in range(ord('a'), ord('z')+1)):
36            for char2 in ''.join(chr(j) for j in range(ord('z'), ord('a')-1, -1)):
37                get_path(char1, char2)
38
39        for l, r in zip(source, target):
40            if l != r:
41                price = min_dist[l, r]
42                if price == float('inf'):
43                    return -1
44                
45                total += price
46        
47        return total
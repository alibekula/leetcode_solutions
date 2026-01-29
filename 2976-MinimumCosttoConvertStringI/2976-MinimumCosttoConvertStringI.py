# Last updated: 29.01.2026, 08:06:33
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
12        def get_path(root):
13            heap = [[0, root]]
14
15            while heap:
16                score, node = heapq.heappop(heap)
17
18                for nei, wei in graph[node]:
19
20                    if (root, nei) not in min_dist or min_dist[(root, nei)] > score+wei:
21                        min_dist[(root, nei)] = score + wei
22                        heapq.heappush(heap, [score+wei, nei])
23
24
25        for char1 in ''.join(chr(i) for i in range(ord('a'), ord('z')+1)):
26            get_path(char1)
27
28        for l, r in zip(source, target):
29            if l != r:
30                price = min_dist[(l, r)] if (l, r) in min_dist else float('inf')
31                if price == float('inf'):
32                    return -1
33                
34                total += price
35        
36        return total
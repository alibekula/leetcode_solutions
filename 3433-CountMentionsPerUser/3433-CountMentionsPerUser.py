# Last updated: 12.12.2025, 17:28:34
1import heapq
2class Solution:
3    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
4        heap = []
5        alls = 0
6        online = {user: True for user in range(numberOfUsers)}
7        ans = [0] *numberOfUsers
8
9        for event in events:
10            ev, ts, ids = event
11            ts = int(ts)
12            if ev != 'OFFLINE':
13                ts += 0.000001
14            heapq.heappush(heap, [ts, ev, ids])
15
16        total = 0
17        while heap:
18            ts, ev, ids = heapq.heappop(heap)
19            
20            if ev == 'MESSAGE':
21                if ids == 'ALL':
22                    alls += 1
23                elif ids == 'HERE':
24                    for user in online:
25                        if online[user] is True:
26                            ans[user] += 1
27                else:
28                    for user in ids.split(' '):
29                        ans[int(user[2:])] += 1
30
31            elif ev == 'OFFLINE':
32                heapq.heappush(heap, [ ts+59.9999,'ONLINE', ids])
33                online[int(ids)] = False
34            elif ev == 'ONLINE':
35                online[int(ids)] = True
36
37        
38        for i in range(len(ans)):
39            ans[i] += alls
40        
41        return ans
42                    
43        
44
45
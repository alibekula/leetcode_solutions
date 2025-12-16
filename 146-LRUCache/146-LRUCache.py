# Last updated: 16.12.2025, 19:12:04
1from collections import deque
2class LRUCache:
3
4    def __init__(self, capacity: int):
5        self.dct = {}
6        self.queue = deque([])
7        self.capacity = capacity
8        self.lazy_delete = {}
9        
10
11    def get(self, key: int) -> int:
12        if not self.queue or key not in self.dct:
13            return -1
14        
15        self.queue.append(key)
16        self.lazy_delete[key] = self.lazy_delete.get(key, 0) + 1
17        return self.dct[key]
18
19
20        
21
22    def put(self, key: int, value: int) -> None:
23
24        if key in self.dct:
25            self.dct[key] = value
26            self.queue.append(key)
27            self.lazy_delete[key] = self.lazy_delete.get(key, 0) + 1
28            return
29
30        self.queue.append(key)
31        self.dct[key] = value
32        
33        if len(self.dct) > self.capacity:
34            popped_key = self.queue.popleft()
35
36            while self.lazy_delete.get(popped_key, 0) > 0:
37                self.lazy_delete[popped_key] -= 1
38                popped_key = self.queue.popleft()
39                
40            del self.dct[popped_key]
41
42        
43
44
45# Your LRUCache object will be instantiated and called as such:
46# obj = LRUCache(capacity)
47# param_1 = obj.get(key)
48# obj.put(key,value)
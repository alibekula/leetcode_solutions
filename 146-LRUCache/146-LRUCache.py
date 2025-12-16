# Last updated: 16.12.2025, 20:45:12
1class Node:
2    def __init__(self, key, value, prev=None, next_value=None):
3        self.prev = prev
4        self.next = next_value
5        self.key = key
6        self.value = value
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.capacity = capacity
12        self.dct = {}
13
14        self.head = Node(0, 0)
15        self.tail = Node(0, 0)
16
17        self.head.next = self.tail
18        self.tail.prev = self.head
19        
20    def _remove_node(self, node):
21        p = node.prev
22        n = node.next
23
24        p.next = n
25        n.prev = p
26    
27    def _add_to_end(self, node):
28        p = self.tail.prev
29        p.next = node
30        node.next = self.tail
31        node.prev = p
32        self.tail.prev = node
33
34    def _remove_from_start(self):
35        r = self.head.next
36        n = r.next
37        self.head.next = n
38        n.prev = self.head 
39
40        return r.key
41
42    def get(self, key: int) -> int:
43        if key not in self.dct:
44            return -1
45        
46        node =self.dct[key]
47        self._remove_node(node)
48        self._add_to_end(node)
49
50        return node.value
51
52        
53
54    def put(self, key: int, value: int) -> None:
55
56        new_node = Node(key, value)
57
58        if key in self.dct:
59            old_node = self.dct[key]
60            
61            self.dct[key] = new_node
62
63            self._remove_node(old_node)
64            self._add_to_end(new_node)
65            return 
66        
67        self.dct[key] = new_node
68        self._add_to_end(new_node)
69
70        if len(self.dct) > self.capacity:
71            node_to_delete = self._remove_from_start()
72            del self.dct[node_to_delete]
73        return 
74
75
76
77
78        
79
80
81# Your LRUCache object will be instantiated and called as such:
82# obj = LRUCache(capacity)
83# param_1 = obj.get(key)
84# obj.put(key,value)
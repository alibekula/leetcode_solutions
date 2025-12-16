# Last updated: 16.12.2025, 21:42:51
1class Node:
2    def __init__(self, val, idx, prev=None, next_value=None):
3        self.val = val
4        self.idx = idx
5        self.prev = prev
6        self.next = next_value
7
8class RecentCounter:
9
10    def __init__(self):
11        
12        self.head = Node(-1, 0) 
13        self.tail = Node(-1, 0)
14        
15        self.head.next = self.tail
16        self.tail.prev = self.head
17        
18        self.idx_counter = 0 
19    def _del_node(self):
20        to_delete = self.head.next
21        after_deleted = to_delete.next
22        
23        self.head.next = after_deleted
24        after_deleted.prev = self.head
25
26    def ping(self, t: int) -> int:
27        self.idx_counter += 1
28        
29        new_node = Node(t, self.idx_counter)
30        last_real = self.tail.prev
31        
32        last_real.next = new_node
33        new_node.prev = last_real
34        
35        new_node.next = self.tail
36        self.tail.prev = new_node
37        
38        while self.head.next != self.tail and self.head.next.val < t - 3000:
39            self._del_node()
40            
41        return self.tail.prev.idx - self.head.next.idx + 1
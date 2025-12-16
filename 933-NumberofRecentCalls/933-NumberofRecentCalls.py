# Last updated: 16.12.2025, 22:30:37
1class Node:
2    def __init__(self, val, prev=None, nxt=None):
3        self.val = val
4        self.prev = prev
5        self.next = nxt
6
7
8class RecentCounter:
9
10    def __init__(self):
11        self.head = Node(0)
12        self.tail = Node(0)
13        self.length = 0
14
15        self.head.next = self.tail
16        self.tail.prev = self.head
17        
18    def _del_node(self):
19        self.length -= 1
20
21        node = self.head.next
22        next_node = node.next
23
24        self.head.next = next_node
25        next_node.prev = self.head
26
27        node.next = None
28        node.prev = None
29
30
31    def ping(self, t: int) -> int:
32        self.length += 1
33
34        new_node = Node(t)
35        prev_last = self.tail.prev
36
37        prev_last.next = new_node
38        new_node.prev = prev_last
39
40        new_node.next = self.tail
41        self.tail.prev = new_node
42
43        leftest = self.head.next
44
45        while leftest != self.tail and leftest.val < t - 3000:
46            self._del_node()
47            leftest = self.head.next
48        
49        return self.length
50
51# Your RecentCounter object will be instantiated and called as such:
52# obj = RecentCounter()
53# param_1 = obj.ping(t)
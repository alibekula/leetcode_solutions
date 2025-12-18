# Last updated: 18.12.2025, 17:34:55
1# """
2# This is the interface that allows for creating nested lists.
3# You should not implement it, or speculate about its implementation
4# """
5#class NestedInteger:
6#    def isInteger(self) -> bool:
7#        """
8#        @return True if this NestedInteger holds a single integer, rather than a nested list.
9#        """
10#
11#    def getInteger(self) -> int:
12#        """
13#        @return the single integer that this NestedInteger holds, if it holds a single integer
14#        Return None if this NestedInteger holds a nested list
15#        """
16#
17#    def getList(self) -> [NestedInteger]:
18#        """
19#        @return the nested list that this NestedInteger holds, if it holds a nested list
20#        Return None if this NestedInteger holds a single integer
21#        """
22
23class NestedIterator:
24    def __init__(self, nestedList: [NestedInteger]):
25        self.stack = [iter(nestedList)]
26        self.next_item = None
27        
28    
29    def next(self) -> int:
30        self.curr = self.next_item
31        self.next_item = None
32        return self.curr
33        
34    
35    def hasNext(self) -> bool:
36         
37         while self.stack:
38
39            curr_item = next(self.stack[-1], None)
40
41            if curr_item is None:
42                self.stack.pop()
43                continue
44            
45            if curr_item.isInteger():
46                self.next_item = curr_item.getInteger()
47                return True
48            else:
49                self.stack.append(iter(curr_item.getList()))
50        
51         return False
52
53# Your NestedIterator object will be instantiated and called as such:
54# i, v = NestedIterator(nestedList), []
55# while i.hasNext(): v.append(i.next())
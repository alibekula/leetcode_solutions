# Last updated: 18.12.2025, 17:35:26
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
30    
31        return self.next_item
32        
33    
34    def hasNext(self) -> bool:
35         
36         while self.stack:
37
38            curr_item = next(self.stack[-1], None)
39
40            if curr_item is None:
41                self.stack.pop()
42                continue
43            
44            if curr_item.isInteger():
45                self.next_item = curr_item.getInteger()
46                return True
47            else:
48                self.stack.append(iter(curr_item.getList()))
49        
50         return False
51
52# Your NestedIterator object will be instantiated and called as such:
53# i, v = NestedIterator(nestedList), []
54# while i.hasNext(): v.append(i.next())
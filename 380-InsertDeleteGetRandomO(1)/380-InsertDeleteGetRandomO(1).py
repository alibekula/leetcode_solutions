# Last updated: 16.12.2025, 18:43:19
1from random import choice
2class RandomizedSet:
3
4    def __init__(self):
5        self.dct = {}
6        self.lst = []
7
8    def insert(self, val: int) -> bool:
9        if val in self.dct:
10            return False
11        
12        idx = len(self.lst)
13        self.lst.append(val)
14        self.dct[val] = idx
15        return True
16        
17
18    def remove(self, val: int) -> bool:
19        if val not in self.dct:
20            return False
21        
22        idx = self.dct[val]
23        last_val = self.lst[-1]
24
25        self.lst[-1], self.lst[idx] = self.lst[idx], self.lst[-1]
26        self.dct[last_val] = idx
27
28        self.lst.pop()
29        del self.dct[val]
30        
31        return True
32
33        
34
35    def getRandom(self) -> int:
36        return choice(self.lst)
37        
38
39
40# Your RandomizedSet object will be instantiated and called as such:
41# obj = RandomizedSet()
42# param_1 = obj.insert(val)
43# param_2 = obj.remove(val)
44# param_3 = obj.getRandom()
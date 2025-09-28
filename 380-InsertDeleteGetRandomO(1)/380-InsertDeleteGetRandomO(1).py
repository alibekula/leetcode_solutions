# Last updated: 28.09.2025, 09:26:25
from collections import defaultdict
from random import choice
class RandomizedSet:

    def __init__(self):
        self.dct = {} # key(value) -> value(idx)
        self.lst = list()

    def insert(self, val: int) -> bool:

        if val in self.dct:
            return False
        idx = len(self.lst)

        self.dct[val] = idx
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.dct:
            return False
        
        idx = self.dct[val]
        last_item = self.lst.pop()
        del self.dct[val]

        if not self.lst or idx == len(self.lst):
            return True

        self.lst[idx] = last_item
        self.dct[last_item] = idx


        return True
        

    def getRandom(self) -> int:
        return choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
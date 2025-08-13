# Last updated: 13.08.2025, 16:57:38
class RandomizedSet:
    from random import choice

    def __init__(self):
        self.dct = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False

        self.dct[val] = len(self.lst)
        self.lst.append(val)

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False
        
        if not self.lst:
            return False

        idx = self.dct[val]
        last = self.lst[-1]

        self.dct[last] = idx
        self.lst[idx] = last

        self.lst.pop()
        del self.dct[val]

        return True

    def getRandom(self) -> int:
        return choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
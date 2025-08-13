# Last updated: 13.08.2025, 16:59:16
class LRUCache:

    def __init__(self, capacity: int):
        self.dct = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        
        val = self.dct.pop(key)
        self.dct[key] = val

        return val

        

    def put(self, key: int, value: int) -> None:

        if (len(self.dct) == self.capacity) and (key not in self.dct):
            iterator = iter(self.dct)
            key_to_remove = next(iterator)
            del self.dct[key_to_remove]
        
        if key in self.dct:
            old_val = self.dct.pop(key)
            self.dct[key] = value
        else:
            self.dct[key] = value
        
        return 


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
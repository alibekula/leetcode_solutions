# Last updated: 12.09.2025, 05:50:21
class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.dct:
            self.dct[key] = []

        self.dct[key].append([timestamp, value])
    
    def search(self, key, ts):

        if key not in self.dct or not self.dct[key]:
            return 

        array = self.dct[key]

        if array[0][0] > ts:
            return

        l, r = 0, len(array)-1
        ans = -1

        while l <= r:

            mid = (l+r)//2
            mid_val = array[mid][0]

            if mid_val <= ts:

                if mid_val == ts:
                    return array[mid][1]

                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return array[ans][1]

        
    def get(self, key: str, timestamp: int) -> str:
        val = self.search(key, timestamp)
        
        return val if val else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
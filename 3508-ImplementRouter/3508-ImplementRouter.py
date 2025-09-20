# Last updated: 20.09.2025, 21:53:03
from collections import deque, defaultdict
class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.router = deque([])
        self.dupl = set()
        self.dest = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:

        packet = (source, destination, timestamp)
        
        if packet in self.dupl:
            return False

        self.router.append(packet)
        self.dupl.add(packet)
        self.dest[destination].append(packet)

        while len(self.router) > self.memoryLimit:
            old_packet = self.router.popleft()
            self.dest[old_packet[1]].popleft()
            self.dupl.remove(old_packet)

        return True

    def forwardPacket(self) -> List[int]:

        if not self.router:
            return []

        packet = self.router.popleft()
        self.dest[packet[1]].popleft()
        self.dupl.remove(packet)
        return list(packet)
        
    def search(self, arr, time, left=True):

        l, r = 0, len(arr)

        while l < r:
            mid = (l+r)//2

            if left:
                if arr[mid][2] >= time:
                    r = mid 
                else:
                    l = mid + 1
            else:
                if arr[mid][2] <= time:
                    l = mid + 1
                else:
                    r = mid 
            
        return l

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        last_idx = self.search(self.dest[destination], endTime, left=False)
        fisrt_idx = self.search(self.dest[destination], startTime, left=True)
        return last_idx - fisrt_idx

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
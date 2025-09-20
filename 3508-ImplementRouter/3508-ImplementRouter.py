# Last updated: 20.09.2025, 22:02:18
from collections import deque, defaultdict

class Router:

    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.router = deque([])
        self.dupl = set()
        self.dest = defaultdict(list)

    def addPacket(self, source, destination, timestamp):
        packet = (source, destination, timestamp)
        if packet in self.dupl:
            return False
        self.router.append(packet)
        self.dupl.add(packet)
        self.dest[destination].append(packet)
        while len(self.router) > self.memoryLimit:
            old_packet = self.router.popleft()
            self.dest[old_packet[1]].pop(0)
            self.dupl.remove(old_packet)
        return True

    def forwardPacket(self):
        if not self.router:
            return []
        packet = self.router.popleft()
        self.dest[packet[1]].pop(0)
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

    def getCount(self, destination, startTime, endTime):
        last_idx = self.search(self.dest[destination], endTime, left=False)
        fisrt_idx = self.search(self.dest[destination], startTime, left=True)
        return last_idx - fisrt_idx

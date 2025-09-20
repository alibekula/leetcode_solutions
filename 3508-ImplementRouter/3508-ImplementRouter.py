# Last updated: 20.09.2025, 22:13:08
from collections import deque, defaultdict

class Router:
    def __init__(self, memoryLimit):
        self.size = memoryLimit
        self.router = deque()
        self.dupl = set()
        self.dest = defaultdict(deque)
        self.timestamps = defaultdict(list)

    def addPacket(self, source, destination, timestamp):
        packet = (source, destination, timestamp)
        if packet in self.dupl:
            return False

        if len(self.router) >= self.size:
            self.forwardPacket()

        self.router.append(packet)
        self.dupl.add(packet)
        self.dest[destination].append(packet)
        self.timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.router:
            return []

        packet = self.router.popleft()
        self.dupl.remove(packet)
        d = packet[1]
        self.dest[d].popleft()
        self.timestamps[d].pop(0)
        return list(packet)

    def search(self, arr, time, left=True):
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2
            if left:
                if arr[mid] >= time:
                    r = mid
                else:
                    l = mid + 1
            else:
                if arr[mid] <= time:
                    l = mid + 1
                else:
                    r = mid
        return l

    def getCount(self, destination, startTime, endTime):
        ts = self.timestamps[destination]
        if not ts:
            return 0
        l = self.search(ts, startTime, left=True)
        r = self.search(ts, endTime, left=False)
        return r - l

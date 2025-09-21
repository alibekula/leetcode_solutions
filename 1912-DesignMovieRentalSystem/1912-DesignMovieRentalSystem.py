# Last updated: 22.09.2025, 04:14:54
from collections import deque, defaultdict
from typing import List

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

        # Add the new packet
        self.router.append(packet)
        self.dupl.add(packet)
        self.dest[destination].append(packet)

        # Enforce memory limit: remove oldest packets if memory limit is exceeded
        while len(self.router) > self.memoryLimit:
            oldest_packet = self.router.popleft() # Remove from main queue
            self.dupl.remove(oldest_packet)      # Remove from duplicate set
            
            # Remove from the destination-specific queue
            # Since packets are added chronologically and popped from the left of `self.router`,
            # the corresponding packet in `self.dest[oldest_packet[1]]` will also be at its left.
            self.dest[oldest_packet[1]].popleft()

        return True

    def forwardPacket(self) -> List[int]:
        if not self.router:
            return []

        # If addPacket already enforces memory limit, this loop is largely redundant,
        # as len(self.router) will generally not exceed self.memoryLimit.
        # However, keeping it doesn't harm correctness and provides a safeguard.
        while len(self.router) > self.memoryLimit:
            packet_to_remove = self.router.popleft()
            self.dupl.remove(packet_to_remove)
            self.dest[packet_to_remove[1]].popleft()

        if not self.router: # Check again after potential cleanup
            return []

        # Forward the oldest packet
        packet_to_forward = self.router.popleft()
        self.dupl.remove(packet_to_forward)
        self.dest[packet_to_forward[1]].popleft()
        return list(packet_to_forward)
        
    def search(self, arr: deque, time: int, left: bool = True) -> int:
        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2

            if left: # Find first element >= time (lower_bound)
                if arr[mid][2] >= time:
                    r = mid 
                else:
                    l = mid + 1
            else: # Find first element > time (upper_bound)
                if arr[mid][2] <= time:
                    l = mid + 1
                else:
                    r = mid 
            
        return l

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr_for_search = self.dest[destination]

        # last_idx points to the first packet with timestamp > endTime
        last_idx = self.search(arr_for_search, endTime, left=False)
        # fisrt_idx points to the first packet with timestamp >= startTime
        fisrt_idx = self.search(arr_for_search, startTime, left=True)
        
        return last_idx - fisrt_idx

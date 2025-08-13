# Last updated: 13.08.2025, 16:56:54
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        # Add elements to the heap and maintain size at most k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            # Add directly if the heap size is less than k
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            # Replace the smallest if val is larger
            heapq.heapreplace(self.min_heap, val)
        # The root of the heap is the kth largest element
        return self.min_heap[0]

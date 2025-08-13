# Last updated: 13.08.2025, 16:58:36
class heapify:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        self.heap.append(item)
        self.heap_up(len(self.heap)-1)
    
    def heap_up(self, idx):
        parent = (idx-1) // 2

        while idx > 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = (idx-1) // 2

    
    def pop(self):
        val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.heap_down()
        return val
        
    def heap_down(self):
        i = 0
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            
        


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = heapify()
        res = None

        for num in nums:
            heap.push(-num)
        
        for _ in range(k):
            res = -heap.pop()

        return res
        
        
        
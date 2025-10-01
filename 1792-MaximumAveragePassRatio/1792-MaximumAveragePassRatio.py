# Last updated: 01.10.2025, 10:35:17
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        heap = []

        for passed, total in classes:
            curr_score = passed / total
            added_score = (passed + 1) / (total + 1)
            heapq.heappush(heap, [curr_score - added_score, passed+1, total+1])
        
        for student in range(extraStudents):
            neg_score, passed, total = heapq.heappop(heap)
            new_score = (passed + 1) / (total + 1)
            old_score = passed / total

            heapq.heappush(heap, [old_score- new_score, passed + 1, total + 1])
        
        total_score = 0

        for _, passed, total in heap:
            total_score += (passed - 1)/ (total-1)
        
        return total_score / len(classes)
# Last updated: 16.08.2025, 17:36:20
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        n, m = len(nums1), len(nums2)
        length = min(k, n)
        ans = []

        for i in range(length):
            heapq.heappush(heap, [nums1[i] + nums2[0], i, 0])
        
        for _ in range(k):
            if not heap:
                return ans

            _, l, r = heapq.heappop(heap)
            ans.append([nums1[l] , nums2[r]])

            if r + 1 < m:
                heapq.heappush(heap, [nums1[l] + nums2[r+1], l, r+1])

        return ans
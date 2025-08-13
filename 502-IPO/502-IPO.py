# Last updated: 13.08.2025, 20:25:32
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        n, m = len(nums1), len(nums2)

        heap = []
        ans = []
        heapq.heappush(heap, [nums1[0] + nums2[0], 0 , 0])
        sett = set()

        for _ in range(k):
            _, l, r = heapq.heappop(heap)
            ans.append([nums1[l], nums2[r]])

            if l + 1 < n and (l+1, r) not in sett:
                heapq.heappush(heap, [nums1[l+1]+nums2[r], l+1, r])
                sett.add((l+1, r))
            if r + 1 < m and (l, r+1) not in sett:
                heapq.heappush(heap, [nums1[l] + nums2[r+1], l, r+1])
                sett.add((l, r+1))
        return ans

# 1 2 - [1 4, 7 2] - 1 4 [7 2, 1 6, 7 4] 1 6 []
# 0 0 1 0 0 1  2 0 1 1 1
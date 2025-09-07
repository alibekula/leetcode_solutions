# Last updated: 07.09.2025, 21:53:39
from sortedcontainers import SortedList

class Solution:

    def get_median(self, arr):
        
        m = len(arr)
        if m % 2 == 1:
            median = arr[m//2]
        else:
            median = (arr[m//2-1] + arr[m//2])/2

        return median

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        n = len(nums)
        container = SortedList()

        for i in range(k):
            if i < n:
                container.add(nums[i])
        
        l, r = 0, k
        ans = [self.get_median(container)]


        while r < n:
            container.remove(nums[l])
            container.add(nums[r])
            ans.append(self.get_median(container))
            l += 1
            r += 1
        
        return ans
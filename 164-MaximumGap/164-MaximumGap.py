# Last updated: 13.08.2025, 16:59:06
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0
        
        l, r = min(nums), max(nums)

        if l == r:
            return 0
        
        count = {key: (float('inf'), float('-inf')) for key in range(n)}
        
        for num in nums:
            if num == r:
                idx = n-1
            else:
                idx = (num - l)*(n-1)//(r-l)
            
            count[idx] = (min(count[idx][0], num), max(count[idx][1], num))
        
        res = 0
        buskets = []

        for i in range(n):
            if count[i][0] != float('inf'):
                buskets.append([count[i][0], count[i][1]])

        for i in range(1, len(buskets)):
            res = max(res, buskets[i][0] - buskets[i-1][1])

        return res


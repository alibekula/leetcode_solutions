# Last updated: 13.08.2025, 16:59:11
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmax = 1
        currmin = 1

        for num in nums:
            if num == 0:
                currmax, currmin = 1, 1
                continue
            
            tmp = currmax
            currmax = max(num*currmax, num*currmin, num)
            currmin = min(tmp*num, num*currmin, num)
            res = max(res, currmax)
        
        return res
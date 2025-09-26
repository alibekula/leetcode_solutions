# Last updated: 27.09.2025, 00:01:18
from math import factorial as F

class Solution:
    def permutations(self, n, k):
        return F(n) / (F(k) * F(n - k))

    def triangleNumber(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0

        nums.sort()
        n = len(nums)
        total = 0

        for k in range(n-1, 1, -1):
            i, j = 0, k-1

            while i < j:

                if nums[i] + nums[j] > nums[k]:
                    total += j - i
                    j -= 1
                else:
                    i += 1
                    
        return total

            


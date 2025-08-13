# Last updated: 13.08.2025, 16:58:24
from math import ceil
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = ceil(n/3)
        num1, num2 = None, None
        count1, count2 = 0, 0
        ans = []

        for num in nums:
            if num == num1:
                count1 += 1
            elif num ==num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                count2 = 1
                num2 = num
            else:
                count1 -= 1
                count2 -= 1

        dct = {num1: 0, num2: 0}

        for num in nums:
            if num in dct:
                dct[num] += 1
        
        for key, value in dct.items():
            if value > n//3:
                ans.append(key)
        
        return ans

        
        
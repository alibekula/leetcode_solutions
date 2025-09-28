# Last updated: 28.09.2025, 07:38:46
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 3:
            return 0 

        nums.sort(reverse=True)

        for i in range(2, n):
            a, b, c = nums[i-2], nums[i-1], nums[i]

            if b + c > a:
                return a+b+c
        
        return 0
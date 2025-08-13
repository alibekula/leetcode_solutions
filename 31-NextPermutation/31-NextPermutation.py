# Last updated: 13.08.2025, 17:01:03
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        
        for i in range(n, 0, -1):

            if nums[i] > nums[i-1]:
                
                for j in range(n, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                
                while n > i:
                    nums[i], nums[n] = nums[n], nums[i]
                    n -= 1
                    i += 1
                
                return
        
        nums.reverse()
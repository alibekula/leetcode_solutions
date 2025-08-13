# Last updated: 13.08.2025, 16:58:25
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        l, r = 0, 0
        ans = []

        while r < len(nums):

            while r+1 < len(nums) and nums[r] == nums[r+1]-1:
                r += 1
            
            if l == r:
                ans.append(f'{nums[r]}')

            else:
                ans.append(f'{nums[l]}->{nums[r]}')

            r += 1
            l = r
        

        return ans

        
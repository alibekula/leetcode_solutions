# Last updated: 13.08.2025, 17:00:01
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def func(i, s):
            if i >= len(nums):
                res.append(s[:])
                return 
            s.append(nums[i])
            func(i + 1, s)

            while i + 1!= len(nums) and nums[i] == nums[i+1]:
                i += 1

            s.pop()
            
            func(i+1, s)

        func(0, [])
        return res

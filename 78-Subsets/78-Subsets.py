# Last updated: 13.08.2025, 17:00:13
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def fn(i, s):
            if i == len(nums):
                res.append(s[:])
                return 
            
            s.append(nums[i])
            fn(i+1, s)
            s.pop()
            fn(i+1, s)
        fn(0, [])
        
        return res




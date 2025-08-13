# Last updated: 13.08.2025, 17:00:48
class Solution:
    from math import factorial
    def permute(self, nums: List[int]) -> List[List[int]]:
        total = factorial(len(nums))
        ans = []
        def comb(path=None):

            path = path if path is not None else []
        
            if total == len(ans):
                return

            if len(nums) == len(path):
                ans.append(list(path))
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    comb(path)
                    val = path.pop()

        comb()

        return ans
            

        
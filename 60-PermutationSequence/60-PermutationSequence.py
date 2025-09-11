# Last updated: 12.09.2025, 04:33:59
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        nums = list(range(1, n+1))
        fact = factorial(n) // n
        k -= 1
        res = []

        while nums:
            idx = k // fact
            res.append(nums[idx])
            nums.pop(idx)
            if not nums:
                break
            
            k %= fact
            fact //= len(nums)
        
        return ''.join(map(str, res))
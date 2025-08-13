# Last updated: 13.08.2025, 16:56:06
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        total = 0
        n = len(nums)
        dp = [0]*(n+1)
        k = 0

        for i in range(n):
            curr = nums[i]

            while total + dp[i] < curr:
                k += 1


                if k > len(queries):
                    return -1
                
                l, r, val = queries[k-1]
                if r >= i:
                    dp[max(l, i)] += val
                    dp[r+1] -= val

            total += dp[i]

        return k
                

        
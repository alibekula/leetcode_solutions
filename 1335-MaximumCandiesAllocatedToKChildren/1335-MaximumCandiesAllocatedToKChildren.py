# Last updated: 13.08.2025, 16:56:32
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)

        def helper(div):
            if div == 0:
                return True

            count = 0
            for c in candies:
                count += c // div
                if count >= k:
                    return True

            return False


        l, r = 0, total//k
        max_val = float('-inf')
        while l <= r:
            mid = (l+r)//2

            if helper(mid):
                l = mid + 1
                max_val = max(max_val, mid)
            else:
                r = mid - 1

        return max_val if max_val != float('-inf') else 0
        
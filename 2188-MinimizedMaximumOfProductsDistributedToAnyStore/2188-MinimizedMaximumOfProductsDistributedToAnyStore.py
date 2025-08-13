# Last updated: 13.08.2025, 16:56:21
class Solution:
    from math import ceil
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def isvalidnum(num):
            req_stores = 0

            for q in quantities:
                req_stores += ceil(q/num)
            
            return True if req_stores <= n else False
        
        l, r = 1, max(quantities)

        while l < r:
            mid = (r + l) // 2

            if isvalidnum(mid):
                r = mid
            else:
                l = mid + 1
        
        return r


        
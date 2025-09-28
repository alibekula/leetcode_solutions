# Last updated: 28.09.2025, 10:31:59
class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        
        n, m = len(f), len(s)

        if n == 0 or m == 0:
            return []
        
        l, r = 0, 0
        ans = []

        while l < n and r < m:
            
            start1, end1 = f[l]
            start2, end2 = s[r]

            left = max(start1, start2)
            right = min(end1, end2)

            if left <= right:
                ans.append([left, right])
            
            if end1 < end2:
                l += 1
            else:
                r += 1
        
        return ans
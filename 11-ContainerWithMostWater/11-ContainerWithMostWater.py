# Last updated: 04.10.2025, 11:17:20
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        l, r = 0, n-1
        total = 0

        while l < r:
            
            left_val = height[l]
            right_val = height[r]
            total = max(total, min(left_val, right_val) * (r - l))

            if left_val <= right_val:
                l += 1
            else:
                r -= 1
        
        return total



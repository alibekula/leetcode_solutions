# Last updated: 13.08.2025, 17:01:26
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_count = 0

        while l <= r:
            if height[l] <= height[r]:
                max_count = max(max_count, height[l] * (r-l))
                l += 1
            else:
                max_count = max(max_count, height[r] * (r-l))
                r -= 1

        return max_count
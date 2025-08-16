# Last updated: 16.08.2025, 17:20:19
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        total = 0
        left_max = height[l]
        right_max = height[r]

        while l <= r:

            if left_max <= right_max:
                left_max = max(height[l], left_max)
                total += max(0, min(left_max, right_max) - height[l])
                l += 1
            else:
                right_max = max(height[r], right_max)
                total += max(0, min(left_max, right_max) - height[r])
                r -= 1

        return total

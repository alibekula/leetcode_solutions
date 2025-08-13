# Last updated: 13.08.2025, 17:00:51
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        height_left, height_right = height[left], height[right]
        total = 0


        while left <= right:
            if height_left <= height_right:
                diff = height_left - height[left]
                height_left = max(height_left, height[left])
                total = max(total, total + diff)
                left += 1
            else:
                diff = height_right - height[right]
                height_right = max(height_right, height[right])
                total = max(total, total + diff)
                right -= 1

        return total
        
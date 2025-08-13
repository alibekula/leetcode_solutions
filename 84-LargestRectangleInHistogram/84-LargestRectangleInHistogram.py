# Last updated: 13.08.2025, 17:00:07
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_h = 0
        heights.append(0)

        for i, h in enumerate(heights):
            
            while stack and heights[stack[-1]] > h:
                curr_h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_h = max( max_h, width * curr_h)
            
            stack.append(i)
        
        return max_h

        
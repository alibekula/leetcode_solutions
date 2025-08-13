# Last updated: 13.08.2025, 17:00:05
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h = [0]*len(matrix[0])
        max_area = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            max_area = max(max_area, self.max_hist_rect(h))

        return max_area

    def max_hist_rect(self, hist: list[int]) -> int:
        max_area = 0
        stack = []
        hist.append(0)

        for i, h in enumerate(hist):

            while stack and hist[stack[-1]] > h:
                curr_h = hist[stack.pop()] 
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, width*curr_h)

            stack.append(i)
        

        return max_area
            
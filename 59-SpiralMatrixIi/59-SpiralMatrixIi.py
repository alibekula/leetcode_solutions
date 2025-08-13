# Last updated: 13.08.2025, 17:00:34
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n-1
        top, bottom = 0, n - 1
        ans = [[0]*n for i in range(n)]
        curr = 1
        total = n ** 2

        while curr <= total:
            
            for col in range(left, right+1):
                ans[top][col] = curr
                curr += 1
            
            top += 1

            for row in range(top, bottom+1):
                ans[row][right] = curr
                curr += 1
            
            right -= 1

            for col in range(right, left-1, -1):
                ans[bottom][col] = curr
                curr += 1
            
            bottom -= 1

            for row in range(bottom, top-1, -1):
                ans[row][left] = curr
                curr += 1
            
            left += 1
        
        return ans
        
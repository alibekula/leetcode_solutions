# Last updated: 13.08.2025, 17:00:40
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []

        while left <= right and up <= down:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            
            up += 1

            for j in range(up, down+1):
                res.append(matrix[j][right])
            
            right -= 1

            if up <= down:
                for n in range(right, left-1, -1):
                    res.append(matrix[down][n])
                
                down -= 1
            
            if left <= right:
                for m in range(down, up-1, -1):
                    res.append(matrix[m][left])
                
                left += 1
            
        return res
        


# Last updated: 13.08.2025, 17:00:19
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_pos = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros_pos.append([i, j])
        
        for x, y in zeros_pos:

            for col in range(0, len(matrix[0])):
                matrix[x][col] = 0
            
            for row in range(0, len(matrix)):
                matrix[row][y] = 0
        
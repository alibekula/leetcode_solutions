# Last updated: 13.08.2025, 16:58:15
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n, m = len(matrix), len(matrix[0])
        i, j = 0, m-1

        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                j -= 1

            if matrix[i][j] < target:
                i += 1

        return False 



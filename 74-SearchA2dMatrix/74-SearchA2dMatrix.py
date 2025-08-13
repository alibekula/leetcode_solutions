# Last updated: 13.08.2025, 17:00:18
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (r-l)//2 + l
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break
        if l > r:
            return False
        l_target = 0
        r_target = len(matrix[mid]) -1
        while l_target <= r_target:
            mid_target = (r_target-l_target)//2 + l_target 
            if matrix[mid][mid_target] == target:
                return True
            elif matrix[mid][mid_target] < target:
                l_target = mid_target + 1
            else:
                r_target = mid_target - 1
        return False
        
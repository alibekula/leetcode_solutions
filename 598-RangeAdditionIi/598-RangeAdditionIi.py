# Last updated: 13.08.2025, 16:57:10
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not m or not n:
            return 0
        
        if not ops:
            return m * n 
            
        min_x, min_y = min(ops, key= lambda x: x[0]), min(ops, key = lambda x: x[1])
        return min_x[0] * min_y[1]
        
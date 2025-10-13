# Last updated: 13.10.2025, 16:18:03
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        left.sort()
        right.sort()
        l = right[0] if right else n
        r = left[-1] if left else 0

        return max(r , n - l)

 



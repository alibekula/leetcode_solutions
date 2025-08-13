# Last updated: 13.08.2025, 17:00:23
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        if n == 2:
            return 2
            
        lst= [0] * (n+1)
        lst[0] = 0
        lst[1] = 1
        lst[2] = 2

        for i in range(3, n+1):
            lst[i] = lst[i-1] + lst[i-2]

        return lst[n]
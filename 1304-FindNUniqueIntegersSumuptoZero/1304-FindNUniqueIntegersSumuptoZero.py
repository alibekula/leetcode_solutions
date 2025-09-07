# Last updated: 07.09.2025, 21:06:40


class Solution:
    
    def __init__(self):
        self.memo = {}

    def sumZero(self, n: int) -> List[int]:
        ans = []

        if n in self.memo:
            return self.memo[n]
        
        if n % 2 == 1:
            ans.append(0)
        
        for i in range(1, n // 2+1):
            ans.append(i)
            ans.append(-i)
        
        self.memo[n] = ans

        return ans
        
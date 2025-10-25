# Last updated: 26.10.2025, 04:20:15
class Solution:
    def totalMoney(self, n: int) -> int:

        seven = ((7 +  1) * 7) // 2 
        
        first = n // 7 
        second = n % 7
        total = ((first) * (first - 1))// 2 * 7 + seven * first
        # 0 7 14 21

        for i in range(1, second+1):
            total += i + first
        
        return total



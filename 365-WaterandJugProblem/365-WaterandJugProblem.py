# Last updated: 08.10.2025, 16:02:57
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)
        
        GCD = gcd(x, y)

        if target <= x + y and target % GCD ==0:
            return True
        
        return False
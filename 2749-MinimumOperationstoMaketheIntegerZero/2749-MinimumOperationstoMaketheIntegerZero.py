# Last updated: 28.09.2025, 05:24:33
class Solution:

    def is_presentable(self, i, num):

        lower = bin(num).count('1') 
        return lower <= i <= num

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        for i in range(1, 61):
            diff= num2 * i
            num = num1 - diff
            if self.is_presentable(i, num):
                return i
        
        return -1 

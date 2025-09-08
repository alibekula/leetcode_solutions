# Last updated: 08.09.2025, 17:27:44
class Solution:
    def check(self, num):

        while num // 10 > 0:
            last = num % 10
            if last == 0:
                return False
            num //= 10
        
        return num != 0

    def getNoZeroIntegers(self, n: int) -> List[int]:

        for i in range(n-1, 0, -1):
            j = n - i

            if self.check(i) and self.check(j):
                return [i, j]
        
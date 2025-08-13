# Last updated: 13.08.2025, 16:56:42
class Solution:
    dct = {0:0, 1:1, 2:1}

    def fib(self, n: int) -> int:
        if n in self.dct:
            return self.dct[n]
        else:
            self.dct[n] = self.dct[n-1] + self.dct[n-2]
        return self.fib(n)

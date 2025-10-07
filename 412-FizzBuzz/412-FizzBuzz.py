# Last updated: 07.10.2025, 20:27:54
class Solution:
    def __init__(self):
        self.memo = {}
        self.m = 0
    def fizzBuzz(self, n: int) -> List[str]:

        if self.m >= n:
            ans = []

            for key in range(1, n+1):
                ans.append(self.memo[key])
            return ans
            
        start = self.m

        for i in range(start + 1, n+1):
            self.m += 1
            if i % 3 == 0 and i % 5 == 0:
                self.memo[i] = 'FizzBuzz'
            elif i % 3 == 0:
                self.memo[i] = 'Fizz'
            elif i % 5 == 0:
                self.memo[i] = 'Buzz'
            else:
                self.memo[i] = str(i)
        
        return self.fizzBuzz(n)

        
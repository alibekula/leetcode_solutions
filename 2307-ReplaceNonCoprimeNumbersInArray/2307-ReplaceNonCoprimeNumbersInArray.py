# Last updated: 23.09.2025, 16:40:29
class Solution:

    def LCM(self, a, b):
        gcd = self.GCD(a, b)

        return (a * b)//gcd 
    
    def GCD(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a


    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        stack = []
        
        for num in nums:
            stack.append(num)
            while len(stack) >= 2:
                g = self.GCD(stack[-1], stack[-2])
                if g == 1:
                    break
                lcm = self.LCM(stack[-1],  stack[-2])
                stack.pop()
                stack.pop()
                stack.append(lcm)
        
        return stack
        
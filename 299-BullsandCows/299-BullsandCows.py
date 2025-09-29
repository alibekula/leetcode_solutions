# Last updated: 29.09.2025, 13:43:44
from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secret = list(secret)
        guess = list(guess)
        idxs = set()

        for idx, nums in enumerate(zip(secret, guess)):
            num1, num2 = nums

            if num1 == num2:
                idxs.add(idx)
        
        bulls = len(idxs)


        counter1 = {}
        counter2 = {}

        for idx, num in enumerate(secret):
            if idx in idxs:
                continue 
            
            counter1[num] = counter1.get(num, 0) + 1
        
        for idx, num in enumerate(guess):
            if idx in idxs:
                continue
            
            counter2[num] = counter2.get(num, 0) + 1
        
        cows = 0

        for key in counter1:
            if key in counter2:
                cows += min(counter1[key], counter2[key])
        
        return f'{bulls}A{cows}B'



        
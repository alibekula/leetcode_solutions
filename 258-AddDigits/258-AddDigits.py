# Last updated: 13.08.2025, 16:58:12
class Solution:
    def addDigits(self, num: int) -> int:
        tmp = str(num)
        curr = num

        while curr >= 10:
            curr = sum([int(i) for i in tmp])
            tmp = str(curr)
        
        return curr
# Last updated: 13.08.2025, 16:58:49
class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()


        while n != 1:
            curr = 0

            for num in str(n):
                curr += int(num) ** 2
            n = curr
            if n in sett:
                return False
            sett.add(n)

        return True
            


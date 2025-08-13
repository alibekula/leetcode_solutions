# Last updated: 13.08.2025, 17:01:30
class Solution:
    def reverse(self, x: int) -> int:
        rev_x = 0 
        res = x
        n = 0
        flag = False


        if res < 0:
            res = -res
            flag = True

        tmp = res

        while tmp:
            tmp //= 10
            n += 1

        tmp = res
        n -=1

        while n >= 0:
            rev_x += (tmp%10) * (10 **(n))
            tmp //= 10
            n -= 1

        if not (-2**31 <= rev_x <= 2 ** 31 - 1):
            return 0
        return rev_x if not flag else -rev_x 
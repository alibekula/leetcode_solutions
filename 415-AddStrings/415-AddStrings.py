# Last updated: 13.08.2025, 16:57:31
class Solution:
    from collections import deque
    def addStrings(self, num1: str, num2: str) -> str:
        add = 0
        ans = deque()
        l, r = len(num1)-1, len(num2)-1
        tmp = 0

        while l >= 0 or r >= 0 or add > 0:

            tmp = add

            if l >= 0:
                tmp += int(num1[l])
                l -= 1

            if r >= 0:
                tmp += int(num2[r])
                r -= 1

            if tmp >= 10:
                add = int(str(tmp)[0])
                res = int(str(tmp)[1])
            else:
                add = 0
                res = str(tmp)

            ans.appendleft(str(res))
        
        if add != 0:
            ans.appendleft(str(add))

        return ''.join(ans)

        
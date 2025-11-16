# Last updated: 16.11.2025, 19:00:35
class Solution:
    def numSub(self, s: str) -> int:
        # 1 1 1 1 1 1
        # n + n - 1 + n - 2

        groups = []
        l, r= 0, 0
        n = len(s)

        while r < n:
            count = 0
            while r < n and s[r] == '1':
                r += 1
                count += 1

            if count > 0:
                groups.append(count)

            l = r
            r += 1

        total = 0

        for c in groups:
            total += (c * (c+1)) // 2 
        
        return total % (10 ** 9 + 7 )
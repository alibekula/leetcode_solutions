# Last updated: 09.09.2025, 05:09:08
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        ans = [0]

        for i in range(n):
            temp = reversed(ans)
            ans += [x | (1 << i) for x in temp]
        
        return ans
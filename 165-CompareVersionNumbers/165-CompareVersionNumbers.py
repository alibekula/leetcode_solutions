# Last updated: 14.09.2025, 09:23:55
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        n, m = len(version1), len(version2)
        l, r = 0, 0

        while l < n or r < m:
            
            num1 = '0'

            while l < n and version1[l] !='.':
                num1 += version1[l]
                l += 1
            
            num2 = '0'
            while r < m and version2[r] != '.':
                num2 += version2[r]
                r += 1
            
            num1 = int(num1)
            num2 = int(num2)
            
            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
            else:
                l += 1
                r += 1
        
        return 0

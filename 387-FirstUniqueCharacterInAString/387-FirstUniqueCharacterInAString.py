# Last updated: 13.08.2025, 16:57:35
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}

        for idx, i in enumerate(s):
            if i in dct:
                dct[i][0] += 1
            else:
                dct[i] = [1, idx]
        
        for j in s:
            if j in dct and dct[j][0] == 1:
                return dct[j][1]
        return -1
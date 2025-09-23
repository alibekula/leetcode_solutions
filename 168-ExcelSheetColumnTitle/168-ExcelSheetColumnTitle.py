# Last updated: 23.09.2025, 16:09:31
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        dct = {key: chr(ord('A') + key) for key in range(26)}

        ans = []

        while columnNumber:
            columnNumber -= 1
            key = columnNumber % 26
            columnNumber = columnNumber // 26
            ans.append(dct[key])
        
        ans.reverse()

        return ''.join(ans)

        
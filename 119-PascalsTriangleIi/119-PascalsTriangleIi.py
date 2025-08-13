# Last updated: 13.08.2025, 16:59:39
class Solution:
    dct = {0: [1], 1: [1, 1], 2: [1, 2, 1]}
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in self.dct:
            return self.dct[rowIndex]

        start = max(self.dct.keys())

        for i in range(start, rowIndex+1):
            prev = self.dct[i-1]
            curr = [1] + [prev[j] + prev[j+1] for j in range(len(prev)-1)] + [1]
            self.dct[i] = curr
        
        return self.dct[rowIndex]
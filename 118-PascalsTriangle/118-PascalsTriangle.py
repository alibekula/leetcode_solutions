# Last updated: 13.08.2025, 16:59:40
class Solution:
    dct = {1: [1], 2: [1, 1]}
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows in self.dct:
            tmp = []
            for j in range(1, numRows + 1):
                tmp.append(self.dct[j])
            return tmp

        for i in range(3, numRows+1):
            curr = []
            l, r = 0, 1

            while r < len(self.dct[i-1]):
                curr.append(self.dct[i-1][l] + self.dct[i-1][r])
                l += 1
                r += 1

            self.dct[i] = [1] + curr + [1]
        
        return list(self.dct.values())


        
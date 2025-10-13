# Last updated: 13.10.2025, 16:40:17
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        ans = [0, 0]

        length = n.bit_length()

        for i in range(length):
            if (n >> i) & 1:
                ans[(i +1) % 2] += 1
        
        ans.reverse()

        return ans
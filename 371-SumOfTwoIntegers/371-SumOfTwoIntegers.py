# Last updated: 19.08.2025, 03:37:32
class Solution:
    
    def _add(self, a, b):

        carry = 0
        ans = 0

        for i in range(32):
            bit1 = (a>>i) & 1
            bit2 = (b>>i) & 1

            if bit1 == bit2:
                # 0 - 0
                if bit1 == 0 and bit2 == 0:
                    bit_res = carry
                    carry = 0
                else:
                    bit_res = carry
                    carry = 1
            else:# bit1 != bit2
                if carry:
                    bit_res = 0
                    carry = 1
                else:
                    bit_res = 1
                    carry = 0

            ans |= (bit_res << i) 
        
        return ans


    def getSum(self, a: int, b: int) -> int:
        mask = 2**32-1

        a = mask&a
        b = mask&b

        ans = self._add(a, b)

        if ans >= 2 **31:
            return -(2**32 - ans)
        
        return ans
        
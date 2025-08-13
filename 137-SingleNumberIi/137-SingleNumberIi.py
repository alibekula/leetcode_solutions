# Last updated: 13.08.2025, 16:59:22
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += (num>>i)&1
            
            bit_sum %= 3
            ans |= (bit_sum<<i)
        
        if ans >= 2**31:
            ans -= 2**32
        
        return ans

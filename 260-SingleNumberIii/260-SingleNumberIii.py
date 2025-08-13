# Last updated: 13.08.2025, 16:58:11
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor_all = 0

        for num in nums:
            xor_all ^= num
        
        i = 0

        while (xor_all >> i) & 1 == 0:
            i += 1
        
        a, b = 0, 0

        for num in nums:
            if (num >> i)&1:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
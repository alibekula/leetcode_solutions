# Last updated: 06.09.2025, 21:51:03
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        prefix = [0] * 18
        prefix[0] = 1

        exp = {0: 1, 1: 4}


        def get_prefix(num):
            if num == 0:
                return 0
            
            log4 = (num.bit_length() -1) // 2

            if log4 in exp:
                base = exp[log4]
            else:
                exp[log4] = 4 ** log4

            residual = num - exp[log4] 

            return prefix[log4] + residual * (log4 + 1)
        
        for i in range(1, 18):
            prefix[i] = prefix[i-1] + 3 * 4 ** (i-1) * i + 1
        
        ans = 0

        for q in queries:
            ans += (get_prefix(q[1]) - get_prefix(q[0]-1) + 1)//2
        
        return ans
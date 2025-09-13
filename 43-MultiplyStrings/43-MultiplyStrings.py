# Last updated: 13.09.2025, 15:00:58
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
            
        n, m = len(num1), len(num2)
        ans = [0] * (n+m)

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                pos1, pos2 = i+j+1, i+j
                mult = int(num1[i])* int(num2[j])
                s = ans[pos1] + mult

                ans[pos2] += s // 10
                ans[pos1] = s % 10 
                
        non_zero_idx = 0
        for i in range(n+m):
            if ans[i] != 0:
                non_zero_idx = i
                break
        
        return ''.join(map(str, ans[non_zero_idx:]))
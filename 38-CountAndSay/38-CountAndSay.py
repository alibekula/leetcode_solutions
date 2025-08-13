# Last updated: 13.08.2025, 17:00:56
class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        ans = '1'
        
        for _ in range(n-1):
            l = 0
            new_ans = []
            while l < len(ans):
                num = ans[l]
                count = 0
                while l < len(ans) and num == ans[l]:
                    count += 1
                    l += 1
                
                new_ans.append(str(count) + num)
            
            ans = ''.join(new_ans)

        return ans  
        

        
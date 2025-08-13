# Last updated: 13.08.2025, 17:01:12
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(s='', left=0, right=0):

            if len(s) == 2 * n:
                ans.append(s)
                return
            
            if left < n:
                dfs(s=s+'(', left = left+1, right=right)
            
            if right < left:
                dfs(s=s+')', left=left, right=right+1)
            
            return
        
        dfs()
        return ans
        
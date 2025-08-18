# Last updated: 18.08.2025, 13:07:01
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(curr, s, pos):
            if curr == 0:
                ans.append(s[:])
            
            if curr < 0:
                return 
            
            for i in range(pos, len(candidates)):
                s.append(candidates[i])
                dfs(curr - candidates[i], s, i)
                s.pop()
        
        dfs(target, [],0)

        return ans
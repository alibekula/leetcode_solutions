# Last updated: 19.08.2025, 03:35:30
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(curr, s, pos):

            if curr == 0:
                ans.append(s[:])
            
            for i in range(pos, len(candidates)):

                candidate = candidates[i]
                if i > pos and candidates[i-1] == candidate:
                    continue
                
                if curr - candidate < 0:
                    break
                
                s.append(candidate)

                dfs(curr-candidate, s, i+1)

                s.pop()
        
        dfs(target, [], 0)
        return ans
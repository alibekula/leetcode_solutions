# Last updated: 18.08.2025, 13:10:26
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(curr, s, pos):
            if curr == 0:
                ans.append(s[:])

            
            for i in range(pos, len(candidates)):

                candidate = candidates[i]

                if curr - candidate < 0:
                    break

                s.append(candidate)
                dfs(curr - candidate, s, i)
                s.pop()
        
        dfs(target, [],0)

        return ans
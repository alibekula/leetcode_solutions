# Last updated: 13.08.2025, 17:00:55
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sett = set()
        ans = []

        def dfs(curr, path=None):
            nonlocal target
            
            path = path if path is not None else []

            if tuple(sorted(path)) not in sett and curr == target:
                ans.append(path[:])
                sett.add(tuple(sorted(path)))
            
            if curr > target:
                return

            for num in candidates:
                path.append(num)
                dfs(curr+num, path)
                path.pop()
        
        dfs(0)

        return ans
            

            
        
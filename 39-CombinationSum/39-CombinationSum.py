# Last updated: 18.08.2025, 14:13:59
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def inner(curr, pos, seq = None):
            if curr == 0:
                ans.add(tuple(sorted(seq)))
                return 
            
            if curr < 0:
                return
            
            seq = [] if seq is None else seq
            
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i-1]:
                    continue
                seq.append(candidates[i])
                inner(curr - candidates[i], i+1, seq)
                seq.pop()
        
        inner(target, 0, None)

        return [list(i) for i in ans]

        
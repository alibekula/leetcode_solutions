# Last updated: 18.08.2025, 14:23:48
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(pos, current_combination, remaining_target):
            # Base case: success
            if remaining_target == 0:
                ans.append(current_combination[:])
                return

            # Base case: failure (overshot)
            if remaining_target < 0:
                return

            for i in range(pos, len(candidates)):
                # --- THIS IS THE KEY TO AVOIDING DUPLICATES ---
                # If the current element is the same as the one before it,
                # and we are not at the beginning of the loop for this level,
                # skip it to avoid a duplicate combination.
                if i > pos and candidates[i] == candidates[i-1]:
                    continue
                # -----------------------------------------------
                
                candidate = candidates[i]

                # Optimization: if the current candidate is too large, break
                if remaining_target - candidate < 0:
                    break

                # Choose
                current_combination.append(candidate)
                # Explore (use i + 1 because each number can be used only once)
                dfs(i + 1, current_combination, remaining_target - candidate)
                # Un-choose (backtrack)
                current_combination.pop()

        dfs(0, [], target)
        return ans
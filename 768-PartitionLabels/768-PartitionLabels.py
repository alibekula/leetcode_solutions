# Last updated: 13.08.2025, 16:56:57
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dct = {ch: idx for idx, ch in enumerate(s)}
        ans = []
        prev = -1
        end = 0

        for i, char in enumerate(s):
            end = max(end, dct[char])
            if i == end:
                ans.append(i - prev)
                prev = i
        
        return ans




        
# Last updated: 13.08.2025, 16:58:06
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        dct = {}

        for idx, c in enumerate(citations):
            if c not in dct:
                dct[c] = 0

            dct[c] = idx + 1
        
        res = 0

        for key, value in dct.items():
            res = max(res, min(key, value))
        
        return res

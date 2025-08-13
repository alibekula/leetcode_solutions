# Last updated: 13.08.2025, 17:00:45
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dct = {}

        for s in strs:
            count = [0]*30

            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            
            if key not in dct:
                dct[key] = []
            
            dct[key].append(s)
        
        return list(dct.values())
            

        
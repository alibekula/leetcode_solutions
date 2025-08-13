# Last updated: 13.08.2025, 16:56:04
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        if len(colors) < 1:
            return 0
        
        if len(colors) == 1:
            return 1

        counter = 0
        colors.extend(colors[:k-1])

        l, r = 0, 1

        while r < len(colors):
                
            if colors[r] == colors[r-1]:
                l = r
                r += 1
                continue
            
            r += 1
                            
            if r - l < k:
                continue
            
            counter +=1
            l += 1
        
        return counter

            




        
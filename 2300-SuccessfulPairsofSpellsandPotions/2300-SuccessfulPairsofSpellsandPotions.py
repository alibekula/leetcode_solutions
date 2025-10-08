# Last updated: 08.10.2025, 11:01:51
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        n,m = len(spells), len(potions)

        if n==0 or m ==0:
            return []
        
        spells = [[spell, idx] for idx, spell in enumerate(spells)]
        potions.sort()
        spells.sort(reverse=True)
        ans = [0] * n
        l, r = 0, 0

        while l < n and r < m:
            spell, idx = spells[l]
            potion = potions[r]

            power = spell * potion

            if power >= success:
                ans[idx] = m -r
                l += 1
            else:
                r += 1
        
        return ans


# Last updated: 13.08.2025, 16:56:30
class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        curr = 0

        if not s:
            return 0
        
        tmp = s[0]

        for char in s:
            if tmp == char:
                curr += 1
            else:
                tmp = char
                curr = 1
            count = max(count, curr)

            
        return count

        
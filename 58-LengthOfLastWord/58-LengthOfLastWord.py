# Last updated: 13.08.2025, 17:00:35
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s)-1
        count = 0
        flag = False
        while r>=0:
            if s[r] == ' ':
                if flag:
                    return count
                else:
                    r -= 1
                    continue
            else:
                flag = True
                count += 1
            r -= 1
        return count
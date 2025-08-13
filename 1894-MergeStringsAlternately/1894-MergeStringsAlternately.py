# Last updated: 13.08.2025, 16:56:23
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        ans = []
        while l <= len(word1) -1 and r <= len(word2)-1:
            ans.append(word1[l])
            ans.append(word2[r])
            l += 1
            r += 1
        if len(word1) > len(word2):
            ans.extend(list(word1[l:]))
        elif len(word1) < len(word2):
            ans.extend(list(word2[r:]))
        else:
            return ''.join(ans)
        return ''.join(ans)
        
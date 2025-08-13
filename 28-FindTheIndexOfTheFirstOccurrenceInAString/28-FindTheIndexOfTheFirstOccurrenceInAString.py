# Last updated: 13.08.2025, 17:01:06
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            j = i + len(needle) - 1

            if  j + 1 > len(haystack):
                return - 1
            
            if haystack[i:j+1] == needle:
                return i

        return -1

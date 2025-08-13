# Last updated: 13.08.2025, 16:57:18
class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        ans = ''

        for char in s:
            if char == ' ':
                ans += word[::-1] + ' '
                word = ''
            else:
                word += char
        if word:
            ans += word[::-1]
        return ans

        
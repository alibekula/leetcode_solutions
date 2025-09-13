# Last updated: 13.09.2025, 15:12:38
class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']

        vow_char = {}
        con_char = {}
        max_vow = 0
        max_con = 0

        for char in s:
            if char in vowels:
                vow_char[char] = vow_char.get(char, 0) + 1
                max_vow = max(max_vow, vow_char[char])
            else:
                con_char[char] = con_char.get(char, 0) + 1
                max_con = max(max_con, con_char[char])

        return max_vow + max_con
# Last updated: 13.08.2025, 17:01:24
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        ans = 0
        prev_value = 0  # Previous numeral's integer value
        
        for char in reversed(s):
            curr_value = roman_map[char]
            if curr_value >= prev_value:
                ans += curr_value
            else:
                ans -= curr_value
            prev_value = curr_value
        
        return ans

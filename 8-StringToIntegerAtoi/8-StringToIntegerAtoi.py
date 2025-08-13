# Last updated: 13.08.2025, 17:01:29
class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Define the range of 32-bit signed integers
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 2: Initialize variables
        i = 0
        n = len(s)
        result = 0
        sign = 1  # Default to positive
        
        # Step 3: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 4: Check for the optional '+' or '-' sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 5: Convert the digits to an integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 6: Check for overflow before adding the digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result

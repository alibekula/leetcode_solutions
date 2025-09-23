# Last updated: 23.09.2025, 15:23:11
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 1:
            return str(numerator)

        if numerator == 0:
            return '0'
        
        is_negative = True

        if (numerator < 0 and denominator < 0) or (numerator > 0 and denominator > 0): 
            is_negative = False

        ans = []
        numerator, denominator = abs(numerator), abs(denominator)

        if is_negative == True:
            ans.append('-')

        integer, remainder = numerator//denominator, numerator%denominator

        ans.append(str(integer))

        if remainder == 0:
            return ''.join(ans)
        
        ans.append('.')
        seen = {}

        while remainder:
            if remainder in seen:
                idx= seen[remainder]
                ans.insert(idx, '(')
                ans.append(')')
                break

            seen[remainder] = len(ans)
            remainder *= 10
            integer, remainder = remainder//denominator, remainder%denominator
            ans.append(str(integer))
        
        return ''.join(ans)
        

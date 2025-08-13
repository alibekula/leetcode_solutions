# Last updated: 13.08.2025, 17:01:25
class Solution:
    def intToRoman(self, num: int) -> str:

        x = num
        result = ''

        dct = {
    1:    'I',
    4:    'IV',
    5:    'V',
    9:    'IX',
    10:    'X',
    40:    'XL',
    50:    'L',
    90:    'XC',
    100:    'C',
    400:    'CD',
    500:    'D',
    900:    'CM',
    1000:    'M'
}
        for key, value in reversed(dct.items()):
            while x >= key:
                result += value
                x -= key
        
        return result

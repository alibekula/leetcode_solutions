# Last updated: 13.08.2025, 16:57:26
class Solution:
    def compress(self, chars: List[str]) -> int:

        if not chars:
            return 0

        chars.append('<eol>')
        count = 0
        first_char = chars[0]
        p = 0

        for char in chars:

            if char == first_char:
                count += 1
            else:

                chars[p] = first_char
                p += 1
                first_char = char

                if count != 1:
                    for num in str(count):
                        chars[p] = num
                        p += 1
                
                count = 1
                
        chars.pop()

        return p
        
                



        
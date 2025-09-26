# Last updated: 27.09.2025, 05:23:55
class Solution:
    def compress(self, chars: List[str]) -> int:

        if not chars:
            return 0

        chars.append('<eol>')
        n = len(chars)
        count = 1
        p = 0
        prev = chars[0]

        for i in range(1, n):
            curr = chars[i]

            if prev == curr:
                count += 1
            else:
                chars[p] = prev
                p += 1
                if count != 1:
                    for num in str(count):
                        chars[p] = num
                        p += 1
                
                prev = curr
                count = 1
        
        return p

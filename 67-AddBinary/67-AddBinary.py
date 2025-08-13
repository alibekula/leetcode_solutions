# Last updated: 13.08.2025, 17:00:27
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a)-1, len(b)-1, 0
        ans = []
        curr = 0

        while i >= 0 or j >= 0 or carry:

            curr = carry

            if i >= 0:
                curr += int(a[i])
                i -= 1
            
            if j >= 0:
                curr += int(b[j])
                j -= 1
            
            ans.append(str(curr%2))
            carry = curr//2
        
        return ''.join(reversed(ans))
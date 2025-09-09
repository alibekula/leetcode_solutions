# Last updated: 10.09.2025, 04:23:09
class Solution:

    def isValid(self, string):

        if not string:
            return False

        num =int(string)

        if 0 > num or num > 255:
            return False

        if len(string) > 1 and string[0] == '0':
            return False

        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)

        if n > 12 or n < 4:
            return []

        ans = []

        def backtrack(i, path):
            if len(path) > 4 or (len(path) == 4 and i < n):
                return

            if i >= n and len(path) == 4:
                ans.append('.'.join(path))
                return

            string = ''
            candidates = []

            for j in range(i, i + 3):
                if j < n:
                    string += s[j]
                    next_idx = j + 1

                    if self.isValid(string):
                        candidates.append([string, next_idx])
            
            for candidate, idx in candidates:
                path.append(candidate)

                backtrack(idx, path)

                path.pop()
        
        backtrack(0, [])
        
        return ans


                
            

            


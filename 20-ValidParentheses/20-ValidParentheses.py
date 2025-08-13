# Last updated: 13.08.2025, 17:01:14
class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True 

        dct = {')':'(', ']':'[', '}':'{'}
        sett = set(['(', '[', '{'])
        stack = []

        for bracket in s:
            if bracket in sett:
                stack.append(bracket)
            else:
                if stack and stack[-1] != dct[bracket]:
                    return False
                                
                if not stack:
                    return False
                stack.pop()
        
        return not stack


        
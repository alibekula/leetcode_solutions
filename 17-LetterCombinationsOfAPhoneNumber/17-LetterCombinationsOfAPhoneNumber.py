# Last updated: 13.08.2025, 17:01:19
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        dct = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               "6": 'mno',
               '7': 'pqrs',
               '8': 'tuv', 
               '9': 'wxyz'}
            
        
        ans = []
        count = 1

        for digit in digits:
            count *= len(dct[digit])

        def comb_search(p=0, s=''):

            if count == len(ans):
                return

            if len(s) == len(digits):
                ans.append(s)
                return
            
            if len(s) > len(digits):
                return
            
            if p >= len(digits):
                return

            for i in range(p, len(digits)):
                for char in dct[str(digits[i])]:
                    comb_search(i + 1, s+char)

        comb_search()

        return ans

        
# Last updated: 14.09.2025, 04:55:55
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        case_insensitive = dict()
        vowel_replacement = {}
        vowels = set('aeiuo')

        for word in wordlist:
            template_word = word.lower()
            if template_word not in case_insensitive:
                case_insensitive[template_word] = word
            s = ''
            for char in template_word:
                if char in vowels:
                    char='|'
                
                s += char
            
            if s not in vowel_replacement: 
                vowel_replacement[s] = word
        
        ans = []

        for query in queries:

            if query in exact:
                ans.append(query)
                continue
            
            if query.lower() in case_insensitive:
                ans.append(case_insensitive[query.lower()])
                continue

            s = ''

            for char in query.lower():
                if char in vowels:
                    char = '|'

                s += char
            
            if s in vowel_replacement:
                ans.append(vowel_replacement[s])
                continue
            
            ans.append('')
        
        return ans
                

                

                




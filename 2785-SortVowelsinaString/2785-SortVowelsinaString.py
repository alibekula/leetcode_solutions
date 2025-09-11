# Last updated: 11.09.2025, 07:03:20
class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = set(sorted('aeiouAEIOU'))
        vowel_map = {}
        lst_s = list(s)

        for char in s:
            if char in vowels:
                vowel_map[char] = vowel_map.get(char, 0) + 1
        
        for i in range(len(lst_s)):
            chats_to_del = []
            if lst_s[i] in vowels:
                for new_char, count in sorted(vowel_map.items()):
                    if count > 0:
                        vowel_map[new_char] -= 1
                        lst_s[i] = new_char
                        break
                    else:
                        chats_to_del.append(new_char)
                    
            for del_char in chats_to_del:
                del vowel_map[del_char]
        
        return ''.join(lst_s)




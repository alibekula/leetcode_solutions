# Last updated: 13.08.2025, 16:57:15
class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter1 = Counter(s1)
        l, r = 0, len(s1)-1

        counter2 = Counter(s2[l:r+1])

        difference = 0

        for key, val in counter1.items():
            if key in counter2:
                counter1[key] = counter1[key] - counter2[key]
                difference += 1 if counter1[key] != 0 else 0
            else:
                difference += 1
        
        if difference == 0:
            return True

        while r + 1 < len(s2):
            del_char = s2[l]

            if del_char in counter1:
                if counter1[del_char] == 0:
                    difference += 1
                
                counter1[del_char] += 1

                if counter1[del_char] == 0:
                    difference -= 1
                
            insert_char= s2[r+1]

            if insert_char in counter1:

                if counter1[insert_char] == 0:
                    difference += 1
                
                counter1[insert_char] -= 1

                if counter1[insert_char] == 0:
                    difference -= 1
            
            if difference ==0:
                return True
            
            r += 1
            l += 1
        
        return False

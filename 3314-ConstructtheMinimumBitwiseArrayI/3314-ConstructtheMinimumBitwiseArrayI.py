# Last updated: 20.01.2026, 21:53:46
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4        for num in nums:
5            if num % 2 == 0:
6                ans.append(-1)
7                continue
8            
9            length = num.bit_length()
10            insert = -1
11            
12            for i in range(length):
13                # 1. Выделяем всё, что ПРАВЕЕ бита i
14                # Маска (1 << i) - 1 даст все единицы справа от i
15                right_part = num & ((1 << i) - 1)
16                
17                # 2. Выделяем всё, что ЛЕВЕЕ бита i (включая его самого, но мы его обнулим)
18                # Просто сбрасываем i-й бит и все, что справа
19                left_part = num & ~((1 << (i + 1)) - 1)
20                
21                # 3. Собираем новое число (кандидат x)
22                # Бит i теперь гарантированно 0
23                candidate = left_part | right_part
24                
25                # Проверяем твою идею: подходит ли этот кандидат
26                if (candidate | (candidate + 1)) == num:
27                    if insert == -1 or candidate < insert:
28                        insert = candidate
29                elif (num >> i) & 1 == 0:
30                    # Если встретили ноль в num, то дальше ломать биты 
31                    # нет смысла, так как x | x+1 не заполнит этот ноль
32                    break
33                    
34            ans.append(insert)
35        return ans
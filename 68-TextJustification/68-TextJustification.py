# Last updated: 13.08.2025, 17:00:26
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        i = 0 
        res = []

        while i < n:

            j = i + 1
            len_line = len(words[i])

            while j < n and len_line + (j - i) + len(words[j]) <= maxWidth:
                len_line += len(words[j])
                j += 1

            words_count = j - i
            line = ''

            if j == i or n == j or words_count == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - len_line
                spaces_between = total_spaces//(words_count - 1)
                extra_space = total_spaces%(words_count - 1)

                for p in range(i, j-1):
                    line += words[p] + ' '*spaces_between + ' '*(1 if extra_space > 0 else 0)
                    extra_space -= 1

                line += words[j-1]
            
            res.append(line)
            i = j

        return res

                
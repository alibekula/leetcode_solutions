# Last updated: 13.08.2025, 16:57:28
class Solution:
    from collections import deque
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        sett = set(bank)

        if endGene not in sett:
            return -1
        
        if startGene == endGene:
            return 0
        
        queue = deque([[startGene, 1]])

        while queue:
            gene, count = queue.popleft()

            for idx, char in enumerate(gene):
                for new in 'ACGT':
                    if new == char:
                        continue

                    s = gene[:idx] + new + gene[idx+1:]

                    if s in sett:
                        if s == endGene:
                            return count

                        sett.remove(s)
                        queue.append([s, count+1])

        return -1
        
                


        
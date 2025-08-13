# Last updated: 13.08.2025, 16:57:49
class Solution:
    from collections import deque
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        dct = {}
        ans = []

        for ticket in tickets:
            if ticket[0] not in dct:
                dct[ticket[0]] = []
            dct[ticket[0]].append(ticket[1])
        
        for airport in dct:
            dct[airport] = deque(sorted(dct[airport]))
        
        def bfs(root):
            
            queue = deque([root])

            while queue:
                node = queue.popleft()
                
                while (node in dct) and dct[node]:
                    dest = dct[node].popleft()
                    bfs(dest)
                
                ans.append(node)
        
        bfs('JFK')

        return ans[::-1]
                







        
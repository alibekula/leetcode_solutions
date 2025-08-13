# Last updated: 13.08.2025, 16:57:32
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dct = {}

        def fill_graph(node1, node2, val):

            if node1 in dct:
                dct[node1].append([node2, val])
            else:
                dct[node1] = [[node2, val], [node1, 1]]
            
            if node2 in dct:
                dct[node2].append([node1, 1/val])
            else:
                dct[node2] = [[node1, 1/val], [node2, 1]]
            
        for args, val in zip(equations, values):
            fill_graph(args[0], args[1], val)          

        ans = []

        def search(x, y, prod, sett):
            if x == y:
                return prod
            
            sett.add(x)

            for n, w in dct[x]:
                if n in sett:
                    continue
                
                res = search(n, y, prod*w, sett)

                if res != -1:
                    return res
            
            return -1
            
                
        for x, y in queries:
            if x not in dct or y not in dct:
                ans.append(-1)
            else:
                ans.append(search(x, y, 1, set()))
        
        return ans




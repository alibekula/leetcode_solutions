# Last updated: 13.08.2025, 16:58:45
class Solution:
    from collections import deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {key: value for key, value in zip(range(numCourses), [[] for _ in range(numCourses)])}
        res = []

        for x, y in prerequisites:
            graph[y].append(x)
        
        def topological_sort():

            dct = {u: 0 for u in graph}

            for u in graph:
                for v in graph[u]:
                    dct[v] += 1
            
            queue = deque([u for u in graph if dct[u]==0])

            while queue:
                node = queue.popleft()
                res.append(node)

                for n in graph[node]:
                    dct[n] -= 1

                    if dct[n] == 0:
                        queue.append(n)
                
        topological_sort()

        if len(res) == len(graph):
            return True
        else:
            return False


                
            



        

            
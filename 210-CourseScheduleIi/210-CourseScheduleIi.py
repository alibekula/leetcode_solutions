# Last updated: 13.08.2025, 16:58:41
class Solution:
    from collections import deque
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {key: value for key, value in zip(range(numCourses), [[] for i in range(numCourses)])}

        for x, y in prerequisites:
            graph[y].append(x)
        
        ans = []
        
        def topological_sort():
            
            connections = {u: 0 for u in graph}

            for u in graph:
                for v in graph[u]:
                    connections[v] += 1
            
            queue = deque( [i for i in connections if connections[i] == 0])

            while queue:
                node = queue.popleft()
                ans.append(node)

                for val in graph[node]:
                    connections[val] -= 1
                    if connections[val] == 0:
                        queue.append(val)
                    
            if len(ans) == len(graph):
                return True
            else:
                return False
        
        return ans if topological_sort() else []


        
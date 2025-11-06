# Last updated: 06.11.2025, 13:25:13
class Solution:
    def find(self, node):
        if node == self.roots[node]:
            return node
        
        self.roots[node] = self.find(self.roots[node])

        return self.roots[node]

    def union(self, node1, node2):

        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.roots[root2] = root1
            return True

        return False

    def set_offline(self, node):
        self.is_online[node] = False

    def get_status(self, node):

        if self.is_online[node] is True:
            return node
        else:
            root = self.find(node)
            min_node = self.min_nodes[root]

            if min_node == -1 or self.is_online[min_node]:
                return min_node
            else:
                for new_node in self.root_to_nodes[root]:

                    if self.is_online[new_node] is True:
                        self.min_nodes[root] = new_node
                        return new_node
                        
        self.min_nodes[root] = -1

        return -1
        


    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        self.roots = {i: i for i in range(1, c+1)}
        self.is_online = {node: True for node in self.roots}

        for u, v in connections:
            self.union(u, v)
        
        self.root_to_nodes = {}

        for node in range(1, c+1):
            root = self.find(node)

            if root not in self.root_to_nodes:
                self.root_to_nodes[root] = [node]
            else:
                self.root_to_nodes[root].append(node)

        self.min_nodes = {}

        for root in self.root_to_nodes:
            self.root_to_nodes[root].sort()
            self.min_nodes[root] = self.root_to_nodes[root][0]

        ans = []

        for op, node in queries:
            if op == 1:
                ans.append(self.get_status(node))
            else:
                self.set_offline(node)
            
        return ans
                

        


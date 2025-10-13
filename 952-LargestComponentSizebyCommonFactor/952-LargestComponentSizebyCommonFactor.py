# Last updated: 13.10.2025, 19:41:00
from collections import defaultdict
class Solution:
    def GCD(self, a, b):
        while b > 0:
            a, b = b, a % b
        
        return a
    
    def find(self, node):
        if self.roots[node] == node:
            return node
        
        self.roots[node] = self.find(self.roots[node])
        return self.roots[node]
    
    def union(self, node1, node2):
        
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False
        
        if self.length[root1] >= self.length[root2]:
            self.roots[root2] = root1
            self.length[root1] += self.length[root2]
        else:
            self.roots[root1] = root2
            self.length[root2] += self.length[root1]

        return True
    
    def getPrimeFactors(self, num):

        # 10 
        # lp = 2 3 5
        # 4 6 8 9 10 12 15 25
        lp = []
        nums = [0] * (num + 1)

        for i in range(2, num+1):
            if nums[i] == 0:
                lp.append(i)

            for prime in lp:
                insert = prime * i
                if insert <= num:
                    nums[insert] = insert
        
        return lp

    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)

        self.roots = list(range(max_num + 1))
        self.length = [1] * (max_num + 1)
        
        num_set = set(nums) 

        for num in nums:

            d = 2
            temp = num
            while d * d <= temp:
                if temp % d == 0:
                    self.union(num, d) 
                    while temp % d == 0:
                        temp //= d
                d += 1

            if temp > 1:
                self.union(num, temp)

        component_counts = {}
        max_size = 0
        for num in nums:
            root = self.find(num)
            component_counts[root] = component_counts.get(root, 0) + 1
            max_size = max(max_size, component_counts[root])
            
        return max_size if nums else 0



            

        
        
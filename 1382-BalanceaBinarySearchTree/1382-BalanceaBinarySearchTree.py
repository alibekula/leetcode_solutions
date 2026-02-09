# Last updated: 09.02.2026, 14:06:29
1class Solution:
2    def balanceBST(self, root: TreeNode) -> TreeNode:
3        # Создаем фиктивный узел (grandparent) для удобства поворотов
4        dummy = TreeNode(0)
5        dummy.right = root
6        
7        # 1. Превращаем дерево в "лозу" (магистраль) через правые повороты
8        def tree_to_vine(grand):
9            count = 0
10            tmp = grand.right
11            while tmp:
12                if tmp.left:
13                    # Правый поворот
14                    old_left = tmp.left
15                    tmp.left = old_left.right
16                    old_left.right = tmp
17                    grand.right = old_left
18                    tmp = old_left
19                else:
20                    count += 1
21                    grand = tmp
22                    tmp = tmp.right
23            return count
24
25        # 2. Левые повороты для создания сбалансированного дерева
26        def compress(grand, m):
27            tmp = grand.right
28            for _ in range(m):
29                # Левый поворот
30                old_right = tmp.right
31                tmp.right = old_right.left
32                old_right.left = tmp
33                grand.right = old_right
34                grand = old_right
35                tmp = grand.right
36
37        # Основная логика DSW
38        n = tree_to_vine(dummy)
39        
40        # Математический расчет количества поворотов
41        import math
42        h = int(math.log2(n + 1))
43        m = 2**h - 1
44        
45        compress(dummy, n - m)
46        while m > 1:
47            m //= 2
48            compress(dummy, m)
49            
50        return dummy.right
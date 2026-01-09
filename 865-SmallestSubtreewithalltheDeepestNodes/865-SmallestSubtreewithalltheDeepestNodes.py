# Last updated: 09.01.2026, 14:26:48
1from collections import deque
2
3class Solution:
4    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
5        if not root:
6            return None
7        
8        # 1. Находим узлы последнего уровня (BFS)
9        queue = deque([root])
10        last_row = []
11        while queue:
12            width = len(queue)
13            last_row = list(queue) # Сохраняем текущий уровень
14            for _ in range(width):
15                node = queue.popleft()
16                if node.left: queue.append(node.left)
17                if node.right: queue.append(node.right)
18        
19        # 2. Функция поиска пути (исправленная)
20        def get_path(curr, target, path):
21            if not curr:
22                return None
23            
24            path.append(curr)
25            
26            if curr is target:
27                return list(path) # Возвращаем копию пути
28            
29            res_left = get_path(curr.left, target, path)
30            if res_left: return res_left # Если нашли слева, пробрасываем наверх
31            
32            res_right = get_path(curr.right, target, path)
33            if res_right: return res_right # Если нашли справа, пробрасываем наверх
34            
35            path.pop() # Backtracking
36            return None
37
38        # 3. Собираем пути для всех глубоких узлов
39        paths = []
40        for node in last_row:
41            paths.append(get_path(root, node, []))
42
43        # 4. Ищем самый глубокий узел, который есть во всех путях
44        # Самый простой способ: берем первый путь и проверяем его узлы с конца
45        common_ancestor = root
46        first_path = paths[0]
47        
48        # Перебираем узлы первого пути с конца к началу
49        for node_to_check in reversed(first_path):
50            is_common = True
51            for p in paths:
52                if node_to_check not in p:
53                    is_common = False
54                    break
55            if is_common:
56                return node_to_check # Это и есть наш искомый LCA
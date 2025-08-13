# Last updated: 13.08.2025, 16:56:46
class Solution:
    from collections import deque
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, m = len(board), len(board[0])
        total = n * m - 1
        graph = {}

        def move_in_matrix(pos, dices=True):
            nonlocal n, m, total
            if dices:
                ans = []
                for i in range(1, 7):
                    newPos = pos + i
                    if newPos <= total:
                        row = n - 1 - (newPos // m)
                        if ((newPos // m) % 2) == 0:
                            col = newPos % m
                        else:
                            col = m - 1 - (newPos % m)
                        ans.append((row, col))
                return ans
            else:
                row = n - 1 - (pos // m)
                if ((pos // m) % 2) == 0:
                    col = pos % m
                else:
                    col = m - 1 - (pos % m)
                return (row, col)

        curr = 0
        while curr <= total:
            node = move_in_matrix(curr, dices=False)
            seq = move_in_matrix(curr, dices=True)
            graph[node] = []
            for x, y in seq:
                if board[x][y] != -1:
                    # Subtract 1 since board values are 1-indexed.
                    graph[node].append(move_in_matrix(board[x][y] - 1, dices=False))
                else:
                    graph[node].append((x, y))
            curr += 1

        # Compute the target cell from the total position.
        target = move_in_matrix(total, dices=False)

        def bfs(root):
            count = 0
            queue = Solution.deque([root])
            visited = set([root])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node == target:
                        return count
                    for nxt in graph.get(node, []):
                        if nxt not in visited:
                            visited.add(nxt)
                            queue.append(nxt)
                count += 1
            return -1

        return bfs(move_in_matrix(0, dices=False))

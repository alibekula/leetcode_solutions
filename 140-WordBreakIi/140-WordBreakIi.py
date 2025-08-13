# Last updated: 13.08.2025, 16:59:19
class Solution:
    def build_tree(self, words):
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word
        return root

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = self.build_tree(wordDict)
        n = len(s)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            res = []
            node = root
            for j in range(i, n):
                if s[j] not in node:
                    break
                node = node[s[j]]
                if '#' in node:
                    word = node['#']
                    if j == n - 1:
                        res.append([word])
                    else:
                        for rest in dfs(j + 1):
                            res.append([word] + rest)
            memo[i] = res
            return res

        all_sentences = dfs(0)
        return [' '.join(words) for words in all_sentences]

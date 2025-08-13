# Last updated: 13.08.2025, 16:59:32
class Solution:
    from collections import deque
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        sett = set(wordList)

        if endWord not in sett:
            return 0
        
        queue = deque([[beginWord, 2]])
        chars = set('qwertyuiopasdfghjklzxcvbnm')

        while queue:
            node, count = queue.popleft()

            for idx, char in enumerate(node):
                for new_char in chars:
                    new_word = node[:idx] + new_char + node[idx+1:]

                    if new_word in sett:
                        if new_word == endWord:
                            return count
                        
                        sett.remove(new_word)
                        queue.append([new_word, count+1])
        
        return 0


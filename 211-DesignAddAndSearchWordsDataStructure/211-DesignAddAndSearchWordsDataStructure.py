# Last updated: 13.08.2025, 16:58:40
class Node:
    def __init__(self):
        self.children = {}
        self.end = False 


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char] 
        node.end = True
        

    def search(self, word: str, idx=0, node=None) -> bool:
        if idx == len(word):
            return node.end
        
        node = node if node is not None else self.root

        if word[idx] == '.':

            for key in node.children.values():
                if self.search(word, idx+1, key):
                    return True
            
        else:
            if word[idx] not in node.children:
                return False
            
            return self.search(word, idx+1, node.children[word[idx]])
        
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
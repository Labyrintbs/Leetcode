#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class Trie:
    def __init__(self):
        #self.node = [None for _ in range(26)]
        self.children = [None] *  26
        self.end = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for char in prefix:
            n = ord(char) - ord("a") #index of char
            if not node.children[n]:
                return None 
            node = node.children[n]
        return node

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            n = ord(char) - ord("a") #index of char
            if not node.children[n]:
                node.children[n] = Trie()
            node = node.children[n]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.end
    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
class WordDictionary(Trie):

    def __init__(self):
        super().__init__()
        
        

    def addWord(self, word: str) -> None:
        self.insert(word)
        

    def search(self, word: str) -> bool:
        def dfs(index: int, node: Trie) -> bool:
            if index == len(word):
                return node.end
            ch = word[index]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(index + 1, child):
                    return True
            else:
                for child in node.children:
                    if child is not None and dfs(index + 1, child):
                        return True
            return False

        return dfs(0, self)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
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



        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end


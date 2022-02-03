class Trie:
    def __init__(self):
        self.word_id = -1
        self.p_ids = []
        self.childs = dict()
            
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = Trie()
        self.init(root, words)
        return self.answer(root, words)
        
    def init(self, root, words):
        for i, w in enumerate(words): 
            self.add(root, w, i)
    
    def add(self, root, word, idx):
        for i, v in enumerate(reversed(word)):
            if v not in root.childs:
                root.childs[v] = Trie()
            if self.is_palindrome(word[:len(word) - i]):
                root.p_ids.append(idx)
            root = root.childs[v]
        root.word_id = idx
            
    def is_palindrome(self, word):
        return word[::] == word[::-1]
    
    def answer(self, root, words):
        results = []
        for i, word in enumerate(words):
            results.extend(self.search(root, word, i))
        return results
            
    def search(self, root, word, i):
        result = []
        
        while word:
            # dcbc + d
            if root.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, root.word_id])
            if not word[0] in root.childs:
                return result
            root = root.childs[word[0]]
            word = word[1:]
        
        # a, a 인경우를 걸러낸다.
        if root.word_id >= 0 and root.word_id != i:
            result.append([i, root.word_id])
        for p_id in root.p_ids:
            result.append([i, p_id])
        return result
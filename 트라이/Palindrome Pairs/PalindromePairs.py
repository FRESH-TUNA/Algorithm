class Trie:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(Trie)
        self.palindrome_ids = []

class Solution:
    root = None
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.init(words)
        return self.answer(words)
    
    def init(self, words):
        self.root = Trie()
        for i, w in enumerate(words): 
            self.add(i, w)

    def add(self, word_idx, word):
        node = self.root
        for char_i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word)-char_i]):
                node.palindrome_ids.append(word_idx)
            node = node.children[char]
        node.word_id = word_idx
        
    def is_palindrome(self, word):
        return word[::] == word[::-1]
    
    def answer(self, words):
        answer = []
        for i, w in enumerate(words): 
            answer.extend(self.search(i, w))
        return answer
            
    def search(self, word_idx, word):
        node, answer = self.root, []
        
        for char_idx, char in enumerate(word):
            if node.word_id >= 0:
                if self.is_palindrome(word[char_idx:]):
                    answer.append([word_idx, node.word_id])    
            if char not in node.children: return answer
            else: node = node.children[char]
        
        if node.word_id >= 0 and node.word_id != word_idx:
            answer.append([word_idx, node.word_id])
            
        for p_id in node.palindrome_ids:
            answer.append([word_idx, p_id])

        return answer
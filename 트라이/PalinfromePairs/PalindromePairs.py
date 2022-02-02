class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.p_word_ids = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            # 단어들의 펠린드롬 여부를 세팅한다.
            if self.is_palindrome(word[0:len(word) -i]):
                node.p_word_ids.append(index)
                
            # 자식의 db로 갱신
            node = node.children[char]
        node.word_id = index
        
    def search(self, index, word):
        result = []
        node = self.root
        
        while word:
            if node.word_id >= 0:
                # 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            
            # 더이상 탐색이 불가능하면 탐색 종료
            if not word[0] in node.children: return result
            
            # 다음 자식 노드로 갱신
            node = node.children[word[0]]
            word = word[1:]
        
        #끝까지 탐색했는데 word_id가 있는 경우
        #같은 단어인 경우 답이 될수 없다. ex: (1, 1)
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        # 끝까지 탐색했는데 palendrom id가 있는 경우
        for p_id in node.p_word_ids:
            result.append([index, p_id])
        return result
            

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(i, word)
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        return results
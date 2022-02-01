# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.root_db = {}
        
    def insert(self, word: str) -> None:
        db = self.root_db
        for c in word[:-1]:
            if not c in db: db[c] = {}
            db = db[c]
    
        last_key_for_sub_tree = word[-1]
        last_key = word[-1].upper()
        if last_key not in db:
            db[last_key] = {}
        if last_key_for_sub_tree not in db:
            db[last_key_for_sub_tree] = {}

        
    def search(self, word: str) -> bool:
        db = self.root_db
        for c in word[:-1]:
            if not c in db: return False
            db = db[c]
            
        return word[-1].upper() in db 


    def startsWith(self, prefix: str) -> bool:
        db = self.root_db
        for c in prefix:
            if not c in db: return False
            db = db[c]
        return True

def solution():
    N, FLOOR = int(input()), "--"
    datas = sorted(input().split()[1:] for _ in range(N))
    trie = dict()
    
    def make_trie():
        for data in datas:
            root = trie
            for datum in data:
                if datum not in root:
                    root[datum] = dict()
                root = root[datum]

    def dfs(root, depth):
        for leaf in root:
            print(FLOOR*depth + leaf)
            dfs(root[leaf], depth+1)
        
    make_trie()
    dfs(trie, 0)

solution()

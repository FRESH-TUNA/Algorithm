import sys, bisect
from functools import cmp_to_key

#global
global N, K, JEWELS, BACKS, REMOVED, BACKS_TREE

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def init():
    # driver
    global N, K, JEWELS, BACKS, REMOVED
    input = sys.stdin.readline
    N, K = map(int, input().split())
    JEWELS = [list(map(int, input().split())) for _ in range(N)]
    BACKS = [int(input()) for _ in range(K)]
    JEWELS.sort(key=cmp_to_key(comparator), reverse=True)

def make_tree():
    global BACKS_TREE
    BACKS_TREE = None
    for back in BACKS: 
        BACKS_TREE = insert(back, BACKS_TREE)

def insert(back, root):
    if root is None: return Node(back)
    if back < root.key:
        root.left = insert(back, root.left)
    else:
        root.right = insert(back, root.right)
    return root

def delete(node, key):
    if node is None: return node
    elif key < node.key:
        node.left = delete(node.left, key)
        return node
    elif key > node.key:
        node.right = delete(node.right, key)
        return node

    if node.left is None and node.right is None:
        return None
    if node.left is None: return node.right
    if node.right is None: return node.left
    
    
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left


    succ_parent, succ = node, node.right
    while succ.left != None:
        succ_parent, succ = succ, succ.left
    if succ_parent != node:
        succ_parent.left = succ.right
    else:
        succ_parent.right = succ.right
    node.key = succ.key
    return node

def solution():
    global BACKS_TREE
    res = 0
    
    for w, v in JEWELS:
        node, target = BACKS_TREE, None  
        while node:
            if node.key >= w:
                target, node = node, node.left
            else: node = node.right
        if target:
            res += v
            BACKS_TREE = delete(BACKS_TREE, target.key)
    print(res)

def comparator(a, b):
    return a[1] - b[1] if a[1] != b[1] else b[0] - a[0]

init()
make_tree()
solution()

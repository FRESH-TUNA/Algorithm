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
    global N, K, JEWELS, BACKS, REMOVED, BACKS_TREE
    input = sys.stdin.readline
    N, K = map(int, input().split())
    JEWELS = [list(map(int, input().split())) for _ in range(N)]
    BACKS = [int(input()) for _ in range(K)]
    JEWELS.sort(key=cmp_to_key(comparator), reverse=True)
    BACKS_TREE = None

def make_tree(): 
    for back in BACKS: insert(back)

def insert(back):
    global BACKS_TREE
    
    if BACKS_TREE is None: 
        BACKS_TREE = Node(back)
        return

    root = BACKS_TREE
    while True:
        if back < root.key:
            if root.left == None:
                root.left = Node(back)
                return
            else: root = root.left
        else:
            if root.right == None:
                root.right = Node(back)
                return
            else: root = root.right

def delete(prev, curr):
    global BACKS_TREE
    if curr.left == None or curr.right == None:
        newCurr = None

        if curr.left == None: newCurr = curr.right
        else: newCurr = curr.left

        if prev == None: BACKS_TREE = newCurr
        elif curr == prev.left: prev.left = newCurr
        else: prev.right = newCurr
    else:
        p, temp = None, curr.right
        while(temp.left != None):
            p, temp = temp, temp.left
        if p != None: p.left = temp.right 
        else: curr.right = temp.right
        curr.key = temp.key

def solution():
    global BACKS_TREE
    res = 0
    
    for w, v in JEWELS:
        node, node_p = BACKS_TREE, None
        target, target_p = None, None
        while node:
            if node.key >= w:
                target_p, target = node_p, node
                node_p, node = node, node.left
            else: node_p, node = node, node.right
        if target:
            res += v
            delete(target_p, target)
    print(res)

def comparator(a, b):
    return a[1] - b[1] if a[1] != b[1] else b[0] - a[0]

init()
make_tree()
solution()
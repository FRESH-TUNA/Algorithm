import sys
from collections import deque

# global
S = None
RES, STACK, LEFT_SET, MAP = set(), [], set(), dict()

def init():
    global S
    input = sys.stdin.readline
    S = input().rstrip()
    sys.setrecursionlimit(1000)

def main():
    make_map()
    dfs(0)
    print('\n'.join(sorted(RES)[1:]))

def make_map():
    left = []
    for i, c in enumerate(S):
        if c == "(": left.append(i)
        elif c == ")": MAP[i] = left.pop()

def dfs(start):
    if start == len(S):
        RES.add(''.join(STACK))
        return

    if S[start] == ")":
        if MAP[start] in LEFT_SET:        
            STACK.append(")")
            dfs(start+1)
            STACK.pop()
        else: dfs(start+1)
    elif S[start] == "(":
        LEFT_SET.add(start); STACK.append("(");
        dfs(start+1)
        LEFT_SET.remove(start); STACK.pop();
        dfs(start+1)
    else:
        STACK.append(S[start])
        dfs(start+1)
        STACK.pop()
    
        
# driver
init()
main()

class Node:
    val, red, blue = 0, None, None
    def __init__(self, val):
        self.val = val

# global
head = Node(0)
node_db = {10: Node(10), 20: Node(20), 
           25: Node(25), 30: Node(30), 40: Node(40)}
blues = {10, 20, 30}
nodes = [head, head, head, head]
dices, ans = None, 0

def dices_init():
    global dices
    dices = list(map(int, input().split()))
    
def circle_init():
    pointer = head
    for n in range(2, 41, 2):
        new_node = node_db[n] if n in node_db else Node(n)
        pointer.red = new_node
        pointer = pointer.red

def west_init():
    pointer = node_db[10]
    pointer.blue = Node(13)
    pointer = pointer.blue
    pointer.red = Node(16)
    pointer = pointer.red
    pointer.red = Node(19)
    pointer = pointer.red
    pointer.red = node_db[25]

def east_init():
    pointer = node_db[30]
    pointer.blue = Node(28)
    pointer = pointer.blue
    pointer.red = Node(27)
    pointer = pointer.red
    pointer.red = Node(26)
    pointer = pointer.red
    pointer.red = node_db[25]

def south_init():
    pointer = node_db[20]
    pointer.blue = Node(22)
    pointer = pointer.blue
    pointer.red = Node(24)
    pointer = pointer.red
    pointer.red = node_db[25]

def north_init():
    pointer = node_db[25]
    pointer.red = Node(30)
    pointer = pointer.red
    pointer.red = Node(35)
    pointer = pointer.red
    pointer.red = node_db[40]

def dfs(idx, res):
    global ans
    if idx == 10:
        ans = max(ans, res)
        return

    for i in range(len(nodes)):
        if not nodes[i]: 
            dfs(idx+1, res)
            continue

        origin_node = nodes[i]
        nodes[i] = nodes[i].blue if nodes[i].val in blues else nodes[i].red
        can_dfs = True

        for _ in range(dices[idx]-1):
            if not nodes[i]: break
            nodes[i] = nodes[i].red
            
        for j in range(4):
            if i == j: continue
            if nodes[j] == nodes[i]:
                can_dfs = False
                break

        if can_dfs:
            sub_ans = res+nodes[i].val if nodes[i] else res
            dfs(idx+1, sub_ans)
        nodes[i] = origin_node
    


# tests
def circle_init_test():
    pointer = head
    while pointer:
        print(pointer.val)
        pointer = pointer.red

def west_north_init_test():
    pointer = node_db[10]
    while pointer:
        print(pointer.val)
        pointer = pointer.red

    print("---")
    pointer = node_db[10]
    print(pointer.val)
    pointer = pointer.blue
    print(pointer.val)
    pointer = pointer.red
    while pointer:
        print(pointer.val)
        pointer = pointer.red

def east_north_init_test():
    pointer = node_db[30]
    while pointer:
        print(pointer.val)
        pointer = pointer.red

    print("---")
    pointer = node_db[30]
    print(pointer.val)
    pointer = pointer.blue
    print(pointer.val)
    pointer = pointer.red
    while pointer:
        print(pointer.val)
        pointer = pointer.red

def south_north_init_test():
    pointer = node_db[20]
    while pointer:
        print(pointer.val)
        pointer = pointer.red

    print("---")
    pointer = node_db[20]
    print(pointer.val)
    pointer = pointer.blue
    print(pointer.val)
    pointer = pointer.red
    while pointer:
        print(pointer.val)
        pointer = pointer.red
    
# driver
dices_init()
circle_init()
west_init()
east_init()
south_init()
north_init()
dfs(0, 0)
print(ans)


import sys

input = sys.stdin.readline
I = int(input())
blocks = [int(input()) for _ in range(I)]
stack, answer = [], max(blocks)

for i in range(I):
    while stack and blocks[stack[-1]]>=blocks[i]:
        height = blocks[stack.pop()]
        width = (i-stack[-1]-1) if stack else i
        answer = max(answer, height*width)
    stack.append(i)

while stack and blocks[stack[-1]]>=blocks[i]:
    height = blocks[stack.pop()]
    width = (I-stack[-1]-1) if stack else I
    answer = max(answer, height*width)    

print(answer)


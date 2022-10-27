def anagram(word):
    WORD_N = len(word)
    stack, db, result = [], set(), []
    traced = [0]*len(word)

    def dfs():
        if len(stack) == WORD_N:
            result.append(''.join(stack))
        for i in range(WORD_N):
            if traced[i]:
                continue
            traced[i] = 1
            stack.append(word[i])
            key = tuple(stack)

            if key not in db:
                db.add(key)
                dfs()

            traced[i] = 0
            stack.pop()
    
    dfs()
    return result

# driver
import sys
N = int(sys.stdin.readline())
WORDS = [sys.stdin.readline().rstrip() for _ in range(N)]

for word in WORDS:
    print('\n'.join(sorted(anagram(word))))


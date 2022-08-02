import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N = int(input())
    ORDER, PREFER = [0]*(N**2), [None]*(N**2)
    G = [[0 for _ in range(N)] for _ in range(N)]
    D, DR, DC = 4, (-1,0,1,0), (0,1,0,-1)

    def prefer_order_init():
        for i in range(N**2):
            j, b1, b2, b3, b4 = map(int, input().split())
            ORDER[i], PREFER[i] = j, {b1, b2, b3, b4}

    def set_students():
        for student, prefer in zip(ORDER, PREFER):
            q = first_step(prefer)
            if len(q) == 1:
                set_student(*q[0], student)
                continue
            q = second_step(q)
            if len(q) == 1:
                set_student(*q[0], student)
                continue
            set_student(*q[0], student)

    def first_step(prefer):
        q, maxadj = deque(), 0
        max_prefers = 0
        
        for r in range(N):
            for c in range(N):
                if G[r][c]: continue

                prefers = 0
                for d in range(D):
                    cr, cc = r+DR[d], c+DC[d]
                    if cr==-1 or cr==N or cc==-1 or cc==N:
                        continue
                    if G[cr][cc] in prefer:
                        prefers += 1
                if prefers > max_prefers:
                    max_prefers = prefers
                    q.clear()
                    q.append((r, c))
                elif prefers == max_prefers:
                    q.append((r, c))
        return q

    def second_step(q):
        max_blanks, nq = 0, deque()
        
        while q:
            r, c = q.popleft()
            blanks = 0

            for d in range(D):
                cr, cc = r+DR[d], c+DC[d]
                if cr==-1 or cr==N or cc==-1 or cc==N:
                    continue
                if not G[cr][cc]:
                    blanks += 1
            if blanks > max_blanks:
                max_blanks = blanks
                nq.clear()
                nq.append((r, c))
            elif blanks == max_blanks:
                nq.append((r, c))
        return nq

    def set_student(r, c, student):
        G[r][c] = student

    def answer():
        db, res = dict(), 0
        score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
        
        for student, prefer in zip(ORDER, PREFER):
            db[student] = prefer

        for r in range(N):
            for c in range(N):
                student, prefers = G[r][c], 0

                for d in range(D):
                    cr, cc = r+DR[d], c+DC[d]
                    if cr==-1 or cr==N or cc==-1 or cc==N:
                        continue
                    if G[cr][cc] in db[student]:
                        prefers += 1
                res += score[prefers]
        print(res)
        
    prefer_order_init()
    set_students()
    answer()

solution()


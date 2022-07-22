def solution():
    N = int(input())
    sand = [list(map(int, input().split())) for _ in range(N)]

    LEFT = [(1, 1, 0.01), (-1, 1, 0.01), 
            (1, 0, 0.07), (-1, 0, 0.07), 
            (1, -1, 0.1), (-1, -1, 0.1), 
            (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), 
            (0, -1, 0)]
    RIGHT = [(x, -y, z) for x,y,z in LEFT]
    DOWN = [(-y, x, z) for x,y,z in LEFT]
    UP = [(y, x, z) for x,y,z in LEFT]
    DISTRIBUTE = [LEFT, DOWN, RIGHT, UP]

    r, c, time = N//2, N//2, 0
    out, DR, DC, DN, GET = [0], [0,1,0,-1], [-1,0,1,0], 4, 0

    # 모래 계산하는 함수
    def distribute(r, c, direction):
        if c < 0: return

        distributed = 0
        for dx, dy, z in direction:
            nx = r + dx
            ny = c + dy
            
            # alpha
            if z == 0:
                new_sand = sand[r][c] - distributed
            else:
                new_sand = int(sand[r][c] * z)
                distributed += new_sand

            if 0<=nx<N and 0<=ny< N:
                sand[nx][ny] += new_sand
            else:
                out[GET] += new_sand

    for i in range(2*N-1):
        d = i % DN
        if d == 0 or d == 2:
            time += 1
        for _ in range(time):
            nr = r + DR[d]
            nc = c + DC[d]
            distribute(nr, nc, DISTRIBUTE[d])  # y좌표, 방향
            r, c = nr, nc
    print(out[GET])

solution()

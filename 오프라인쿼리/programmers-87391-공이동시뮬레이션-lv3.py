def solution(n, m, x, y, queries):
    minx, maxx, miny, maxy = x, x, y, y
    D, DX, DY = 4, (0, 0, -1, 1), (-1, 1, 0, 0)

    for d, w in reversed(queries):
        if d==0:
            maxy += w
            if maxy>=m:
                maxy = m-1
            if miny!=0:
                miny += w
        if d==1:
            miny -= w
            if miny<0:
                miny = 0
            if maxy!=m-1:
                maxy -= w
        if d==2:
            maxx += w
            if maxx>=n:
                maxx = n-1
            if minx!=0:
                minx += w
        if d==3:
            minx -= w
            if minx<0:
                minx = 0
            if maxx!=n-1:
                maxx -= w
                
        if minx>maxx or miny>maxy:
            return 0
    else:
        return (maxx-minx+1) * (maxy-miny+1)


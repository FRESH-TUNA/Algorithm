from itertools import product

def solution():
    N = int(input())
    operators = (" ", "+", "-")

    def make_expr(M, case):
        expr = []
        for m in range(M-1):
            expr.append(str(m+1))
            expr.append(case[m])
        expr.append(str(M))
        return expr

    def make_expr_str(expr):
        return ''.join(expr)
        
    def calculate(expr_str):
        return eval(expr_str.replace(" ", "")) == 0
    
    # driver
    for _ in range(N):
        M = int(input())
        for case in product(operators, repeat=M-1):
            expr_str = make_expr_str(make_expr(M, case))
            if calculate(make_expr_str(make_expr(M, case))):
                print(expr_str)
        print()
     
solution()

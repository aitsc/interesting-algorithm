def solveNQueens(n: int):
    jie = []

    def out(zuobiao):
        jie.append([])
        for x in zuobiao:
            jie[-1].append('.' * x + 'Q' + '.' * (n - x - 1))

    def digui(zuobiao=[]):
        if len(zuobiao) == n:
            out(zuobiao)
        for i in range(n):
            y = False
            for j, x in enumerate(zuobiao):
                if i == x or i == x + (i - j) or i == x - (i - j):
                    y = True
                    break
            if y:
                continue
            digui(zuobiao + [i])

    digui()
    return jie

print(solveNQueens(4))
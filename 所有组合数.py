def combine(List):
    def f(l, c):
        ll = []
        if c == 1:
            return [[i] for i in l]
        for i, x in enumerate(l):
            for j in f(l[i + 1:], c - 1):
                ll.append([x] + j)
        return ll
    a=[]
    for i in range(len(List)+1):
        a+=f(List, i)
    return a

print(combine('abcd'))
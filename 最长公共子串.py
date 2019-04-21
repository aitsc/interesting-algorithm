

def main(x,y):
    if not x or not y:
        return 0
    m=[[0]*(len(y)+1) for i in range(len(x)+1)]
    c=[[0]*(len(y)+1) for i in range(len(x)+1)]
    max_len=0
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            if a==b:
                m[i][j]=m[i-1][j-1]+1
                c[i][j]=a
            max_len=max(max_len,m[i][j])
    return max_len

x='1AB2345CD'
y='12345EF'
print(main(x,y))
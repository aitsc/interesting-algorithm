

def 矩阵连乘问题(p):
    m=[[0]*len(p) for i in range(len(p))]
    b=[[0]*len(p) for i in range(len(p))]
    for r in range(1,len(p)):
        for i in range(len(p)-r):
            j=i+r
            for k in range(i,j):
                s=m[i][k]+m[k+1][j]+p[i][0]*p[k][1]*p[j][1]
                if s<m[i][j] or m[i][j]==0:
                    m[i][j]=s
                    b[i][j]=k

    a=[[0,b[0][-1],len(p)-1]]
    allK=[]
    result=[]
    for i in range(len(p)):
        result.append('')
        result.append(str(i))
    result.append('')

    i=0
    while i<len(a):
        l,k,r=a[i]
        i += 1
        if r==l+1:
            continue
        if l<=k<=r:
            if l<k:
                a.append([l,b[l][k],k])
                result[l * 2] += '('
                result[k * 2+2] = ')' + result[k * 2+2]
            if k<r:
                a.append([k+1, b[k+1][r], r])
                result[(k+1) * 2] += '('
                result[r * 2+2] = ')' + result[r * 2+2]
            allK.append(k)
    print(allK)
    print(''.join(result))


p=[[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]
矩阵连乘问题(p)
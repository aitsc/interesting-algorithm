

def main(w,v,J):
    m=[[0]*(J+1) for i in range(len(w))]
    b=[[0]*(J+1) for i in range(len(w))]
    for i in range(len(w)):
        for j in range(1,J+1):
            if i==0:
                if j>=w[i]:
                    m[i][j]=v[i]
                    b[i][j] = 1
                continue
            if j>=w[i]:
                if m[i-1][j-w[i]]+v[i]>m[i-1][j]:
                    m[i][j] =m[i-1][j-w[i]]+v[i]
                    b[i][j]=1
                else:
                    m[i][j] = m[i-1][j]
            else:
                m[i][j] = m[i - 1][j]


    y=[]
    j=J
    V=0
    for n in range(len(w)-1,-1,-1):
        if b[n][j]!=0:
            y=[n]+y
            j-=w[n]
            V+=v[n]
    print(y)
    print(V)


w=[2,2,6,5,4]
v=[6,3,5,4,6]
J=10
main(w,v,J)
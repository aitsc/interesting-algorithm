

def compute(MN):
    if not MN:
        return [0,0]
    def a(MN_mark,i,j,PQm,x=True):
        # 递归9个方向遍历
        for ii in [i-1,i,i+1]:
            for jj in [j-1,j,j+1]:
                try:
                    if not MN_mark[ii][jj] and MN[ii][jj]:
                        MN_mark[ii][jj]=1
                        PQm[2] += 1
                        a(MN_mark,ii,jj,PQm,False)
                except:...
        # 结束递归得到最大观众数量
        if x:
            if PQm[2]>PQm[1]:
                PQm[1]=PQm[2]
            if PQm[2]>0:
                PQm[0]+=1
            PQm[2]=0

    MN_mark=[[0]*len(MN[0]) for i in range(len(MN))]
    PQm=[0,0,0]
    # 遍历每一个座位
    for i in range(len(MN)):
        for j in range(len(MN[0])):
            a(MN_mark, i, j, PQm, x=True)
    print(PQm[:2])
    return PQm[:2]


MN=[
    [0,0,0,0,1,0,0,1,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
]
MN=[[0]*1000 for i in range(1000)]

compute(MN)
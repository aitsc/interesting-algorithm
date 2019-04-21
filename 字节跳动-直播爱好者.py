

def start(ST,M):
    # 如果为空
    if not ST:
        return 0
    # 如果s>t则补充完整
    for i in range(0,len(ST),2):
        s=ST[i]
        t=ST[i+1]
        if s>t:
            ST[i + 1]=M-s+t
    # 按照结束时间排序
    s_t=sorted([(ST[i],ST[i+1]) for i in range(0,len(ST),2)],key=lambda t:t[1])
    # 贪心算法寻找最优路径
    op=[(-1,0)]
    for i,(s,t) in enumerate(s_t[1:]):
        for j in range(len(op)-1,-1,-1):
            st=s_t[op[j][1]]
            if st[1]<=s:
                op.append((j,i))
                break
    # 还原最优路径
    l=op[-1]
    path=[s_t[l[1]]]
    while l[0]>=0:
        l = op[l[0]]
        path.append(s_t[l[1]])
    # 以24小时为区间寻找最大直播数量
    left=0
    maxL=0
    for i in range(len(path)):
        while path[left][1]-path[i][0]>M:
            maxL=max(maxL,i-left)
            left+=1
    # 如果最大区间没有超过24小时
    if path[0][1]-path[-1][0]<=M:
        maxL=len(path)
    print(maxL)



ST=[0,5,2,7,6,9]
ST=[0,3,3,7,7,0]
M=10
start(ST,M)



def start(cards):
    if not cards:
        return 0
    # 滚动数组
    d_last={0:0}
    # 动态规划
    for i,(x,y) in enumerate(cards):
        d_next = {} # 滚动数组
        for j,v in d_last.items():
            for jj in [j,j+x,abs(j-x)]: # 增加一个卡牌后的可能差值
                if jj in d_next: # 计算过的卡牌
                    continue
                v1=0 if jj not in d_last else d_last[jj]
                v2=0 if jj+x not in d_last else d_last[jj+x]+y
                v3=0 if abs(jj-x) not in d_last else d_last[abs(jj-x)]+y
                d_next[jj]=max(v1,v2,v3)
        d_last=d_next
    print(d_last[0])


start([(3,1),(2,2),(1,4),(1,4)])
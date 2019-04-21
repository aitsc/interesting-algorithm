import copy

def viterbi(matrx,point):
    dis_path_min=[float("inf")]*len(matrx)
    dis_path=[set() for i in range(len(matrx))]
    for i in range(len(matrx)):
        if i==point:
            continue
        dis_path_min[i]=min(dis_path_min[i],matrx[i][point])
        dis_path[i].add(i)
    for k in range(len(matrx)-2):
        dis_path_c=copy.deepcopy(dis_path)
        dis_path_min_c=copy.deepcopy(dis_path_min)
        for i in range(len(matrx)):
            if i==point:
                continue
            min_=float("inf")
            min_p=len(matrx)
            for j in range(len(matrx)):
                if j == point:
                    continue
                if i in dis_path_c[j]:
                    continue
                if min_>matrx[i][j]+dis_path_min_c[j]:
                    min_ = matrx[i][j] + dis_path_min_c[j]
                    min_p=j
            dis_path_min[i]=min_
            if min_!=float("inf"):
                dis_path[i]=copy.copy(dis_path_c[min_p])|{i}
    min_=float("inf")
    for i in range(len(matrx)):
        if i==point:
            continue
        min_=min(min_,dis_path_min[i]+matrx[i][point])
    return min_

if __name__=="__main__":
    matrx=[
        [0, 2, 6, 5],
        [2, 0, 4, 4],
        [6, 4, 0, 2],
        [5, 4, 2, 0],
    ]
    m=float("inf")
    for i in range(len(matrx)):
        m=min(m,viterbi(matrx,i))
    print(m)
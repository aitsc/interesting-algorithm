import copy
import sys
sys.setrecursionlimit(1000000)

# 快速排序
def quickSort(array,l=0,r=-1):
    if r==-1:
        r=len(array)-1
    m=array[l]
    m_th=l
    ll=l
    rr=r
    while ll!=rr:
        if m_th==ll:
            if m>array[rr]:
                array[m_th]=array[rr]
                ll+=1
                m_th=rr
            else:
                rr-=1
        elif m_th==rr:
            if m<array[ll]:
                array[m_th]=array[ll]
                rr-=1
                m_th=ll
            else:
                ll+=1
    array[m_th]=m
    if m_th-l>1:
        quickSort(array, l, m_th - 1)
    if r-m_th>1:
        quickSort(array, m_th + 1, r)
    return array

# 堆排序
def heapSort(array):
    n = len(array)
    for root in range(int(n/2),0,-1):
        while root<=int(n/2):
            l=root*2
            r=root*2+1
            if r>n:
                r=l
            if array[l-1]>array[r-1]:
                if array[l-1]>array[root-1]:
                    array[l - 1], array[root - 1] = array[root-1], array[l-1]
                    root=l
                else:
                    break
            else:
                if array[r-1]>array[root-1]:
                    array[r - 1], array[root - 1] = array[root-1], array[r-1]
                    root=r
                else:
                    break
    while n>1:
        array[0], array[n - 1] = array[n - 1], array[0]
        n=n-1
        root=1
        while root<=int(n/2):
            l=root*2
            r=root*2+1
            if r>n:
                r=l
            if array[l-1]>array[r-1]:
                if array[l-1]>array[root-1]:
                    array[l - 1], array[root - 1] = array[root-1], array[l-1]
                    root=l
                else:
                    break
            else:
                if array[r-1]>array[root-1]:
                    array[r - 1], array[root - 1] = array[root-1], array[r-1]
                    root=r
                else:
                    break
    return array

# 基数排序
def radixSort(array):
    bucket=[[] for i in range(10)]
    hightNum_all=True
    s=1
    while hightNum_all:
        hightNum_all = False
        for i in array:
            if i>s:
                hightNum_all = True
            hightNum=int(i/s)%10
            bucket[hightNum].append(i)
        k=0
        for i in bucket:
            for j in i:
                array[k]=j
                k+=1
        bucket = [[] for i in range(10)]
        s*=10
    return array

# 归并排序
def mergeSort(array,n):
    def f(array,n,l,r):
        if r-l<n or n==1:
            for i in range(l,r):
                m=array[i]
                th=i
                for j in range(i+1,r):
                    if array[j]<m:
                        m=array[j]
                        th=j
                array[i],array[th]=array[th],array[i]
            return
        x=int((r-l)/n)
        for i in range(n-1):
            f(array,n,l+x*i,l+x*(i+1))
        f(array, n, l + x * (n-1), r)
        a=[]
        nl=[0]*n
        while sum(nl)<r-l:
            th=-1
            k=-1
            m=float('inf')
            for i,j in enumerate(nl):
                t=i*x+j+l
                if (j<x or i==n-1) and t<r and array[t]<m:
                    m=array[t]
                    th=t
                    k=i
            if th>=0:
                nl[k]+=1
                a.append(array[th])
        for i in range(l,r):
            array[i]=a[i-l]
    f(array,n,0,len(array))
    return array

# 红黑树

# 哈希表

# 迪杰斯特拉算法
def dijkstra(matrx,point):
    path=[[point] for i in range(len(matrx))]
    point_distince=[float('inf')]*len(matrx)
    point_distince[point]=0
    point_compare=[i for i in range(len(matrx)) if i!=point]
    min_path_point=point
    while len(point_compare)>0:
        min_path_len = float('inf')
        min_path_point_num=0
        for num,i in enumerate(point_compare):
            path_len = matrx[i][min_path_point]+point_distince[min_path_point]
            if path_len<point_distince[i]:
                point_distince[i]=path_len
                path[i]=path[min_path_point]+[i]
            else:
                if path[i][-1]!=i:
                    path[i].append(i)
                path_len=point_distince[i]
            if path_len<min_path_len:
                min_path_len=path_len
                min_path_point_num=num
        min_path_point=point_compare[min_path_point_num]
        del point_compare[min_path_point_num]
    print(path)
    print(point_distince)
    print(point_distince[-1]+matrx[point][path[-1][-1]])

# 弗洛伊德算法


if __name__=="__main__":
    # 迪杰斯特拉算法
    # matrx=[
    #     [0, 6, 3, float('inf'), float('inf'), float('inf'), ],
    #     [6, 0, 2, 5, float('inf'), float('inf'), ],
    #     [3, 2, 0, 3, 4, float('inf'), ],
    #     [float('inf'), 5, 3, 0, 2, 3, ],
    #     [float('inf'), float('inf'), 4, 2, 0, 5, ],
    #     [float('inf'), float('inf'), float('inf'), 3, 5, 0, ],
    # ]
    # point=0
    # dijkstra(matrx, point)

    # 快速排序
    array=[9,8,3,9,1,2,7,5,5]
    print(quickSort(array))

    # 堆排序
    array=[9,8,3,9,1,2,7,5,5]
    print(heapSort(array))

    # 基数排序
    array = [9, 8, 3, 9, 100,1000,102, 2, 7, 5, 5,99]
    print(radixSort(array))

    # 归并排序
    array = [9, 8, 3, 9, 100,1000,102, 2, 7, 5, 5,99]
    print(mergeSort(array,2))
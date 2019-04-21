

def start(a,b):
    if not a:
        return 0
    a_max=float("-inf")
    b_min=float("inf")
    l=0
    s=0
    # 向前推进
    for k,(i,j) in enumerate(zip(a,b)):
        if i>=j: # 如果这个位置a>b
            s+=2**(k-l)-1
            a_max = float("-inf")
            b_min = float("inf")
            l=k+1
            continue
        a_max=max(a_max,i)
        b_min=min(b_min,j)
        if a_max>=b_min: # 如果此时不满足max和min的要求
            s += 2 ** (k - l) - 1
            l += 1
            a_max=max(a[l:k+1])
            b_min=min(b[l:k+1])
            while l<k and a_max>=b_min: # 从后向前推进寻找满足要求的点
                l+=1
                a_max = max(a[l:k + 1])
                b_min = min(b[l:k + 1])
    if a_max < b_min:
        s += 2 ** (k - l+1) - 1
    print(s)



a=[3,2,1,3,1,2,1,1]
b=[3,3,3,3,3,3,3,3]
a=[3,2,1,3,5,3,4]
b=[3,3,3,3,6,6,5]
start(a,b)
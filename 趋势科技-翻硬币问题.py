def start(n,k):
    if n<k or (n%2 and k%2==0):
        print('无解')
        return
    x=n
    y=0
    for i in range(0,n,k):
        print(n-i,i)
        x = n-i
        y = i
    while x!=k and x!=0:
        if x%2:
            x+=k-x-1
        else:
            x+=k-x
        y=n-x
        print(x, y)
    print(0, n)
n=40
k=7
start(n,k)
'''
40 0
33 7
26 14
19 21
12 28
5 35
6 34
7 33
0 40
'''
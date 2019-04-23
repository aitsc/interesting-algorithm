# AC 100%

import heapq
aa,bb=input().strip().split()
if aa=='1' and bb=='1':
    print(0)
else:
    b=True
    s1={}
    s_num1=[0]
    s2={}
    s_num2=[0]
    for i in range(int(aa)):
        a=input().strip().split()
        if b:
            ss1=s1
            ss2=s2
            ss_num1=s_num1
            ss_num2=s_num2
        else:
            ss1=s2
            ss2=s1
            ss_num1=s_num2
            ss_num2=s_num1
        for i in range(0,len(a),2):
            if a[i] in ss1:
                ss1[a[i]]+=1
            else:
                ss1[a[i]]=1
            ss_num1[0]+=1
        for i in range(1,len(a),2):
            if a[i] in ss2:
                ss2[a[i]]+=1
            else:
                ss2[a[i]]=1
            ss_num2[0]+=1
        b=not b

    # s1=sorted(s1.items(),key=lambda t:t[1],reverse=True)
    # s2=sorted(s2.items(),key=lambda t:t[1],reverse=True)
    s1=heapq.nlargest(2, s1.items(), key=lambda t: t[1])
    s2=heapq.nlargest(2, s2.items(), key=lambda t: t[1])

    s_num1=s_num1[0]
    s_num2=s_num2[0]
    if s1[0][0]!=s2[0][0]:
        print(s_num1-s1[0][1]+s_num2-s2[0][1])
    else:
        if len(s1)==1 and len(s2)!=1:
            print(min(s1[0][1],s_num2-s2[1][1]))
        elif len(s1)==1 and len(s2)==1:
            print(min(s_num1,s_num2))
        elif len(s1)!=1 and len(s2)==1:
            print(min(s2[0][1],s_num1-s1[1][1]))
        else:
            print(min(s_num1-s1[0][1]+s_num2-s2[1][1],s_num2-s2[0][1]+s_num1-s1[1][1]))
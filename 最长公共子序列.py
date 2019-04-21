

def main(x,y):
    c=[[0]*(len(y)+1) for i in range(len(x)+1)]
    b=[[0]*(len(y)+1) for i in range(len(x)+1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            try:
                if x[i-1]==y[j-1]:
                    c[i][j]=c[i-1][j-1]+1
                    b[i][j]=x[i-1]
                elif c[i][j-1]>c[i-1][j]:
                    c[i][j]=c[i][j-1]
                    b[i][j]=1
                else:
                    c[i][j]=c[i-1][j]
                    b[i][j]=0
            except:
                print(i,j)
                raise 1

    print(c[len(x)][len(y)])
    s=[[len(x),len(y),b[len(x)][len(y)]]]
    ss=''
    i=0
    continue_times=0
    continue_times_max=0
    while i<len(s):
        l,r,v=s[i]
        if isinstance(v,int):
            continue_times_max=max(continue_times_max,continue_times)
            continue_times=0
            if v==0:
                if l>0:
                    s.append([l-1,r,b[l-1][r]])
            else:
                if r>0:
                    s.append([l, r - 1, b[l][r - 1]])
        else:
            continue_times+=1
            ss=v+ss
            if l>0:
                s.append([l-1, r - 1, b[l-1][r - 1]])
        i+=1
    print(ss)
    print(continue_times_max)


x='bbbbcaccccbacbacaacaccbcabccbcccccccaaaabbbacacccbccaabbaccccccbcacabacbbcabccabbbbcbbbcaababbcbcabbccaaabcbcbcabcaccbbacbabaccbaabaabcbcbabacbabbbcbaaaccac'
y='acacacaacabacccaacabcabcaabaabcabccacbcabbaabcaccbaacbbaccbabcaaccacbcbabccaacbcbbbcababcbabcbbaabaaaacacbaaaaabbcacaccabbbcaaccacacabbaaabbbbccbaaabacbacbcababbaabcccbbbaaabaacbacabacbbbbcacb'
main(x,y)
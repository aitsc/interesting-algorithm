

def compute(sections):
    if not sections:
        return []
    sections=sections.replace(' ','').replace('\n','').replace('\r','')
    s=[(int(i.split(',')[0]),int(i.split(',')[1])) for i in sections.split(';')]
    # 按序号位置排序
    s=sorted(s)
    # 贪心合并
    ss=[(s[0][0],s[0][1])]
    for i,j in s[1:]:
        if ss[-1][0]<i<ss[-1][1] and j>ss[-1][1]:
            i=ss[-1][0]
            del ss[-1]
        ss.append((i,j))
    print(ss)

compute('''1,10;32,45;78,94;5,16;80,100;200,220;16,32''')
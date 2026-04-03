from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    se=set()
    d=Counter(s)
    m=0
    
    for x in s:
        se.add(x)
        d[x]-=1
        if d[x]==0:
            del d[x]
        
        m=max(m, len(se)+len(d))
    print(m)

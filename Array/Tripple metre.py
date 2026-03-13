s,t=map(int,input().split())
c=0
for a in range(s+1):
    for b in range(s+1):
        for d in range(s-a-b+1):
            if a*b*d<=t:
                c+=1
print(c)

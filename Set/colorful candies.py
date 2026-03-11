n,k=map(int, input().split())
a=list(map(int, input().split()))
d={}
l=0
m=0

for r in range(len(a)):
    d[a[r]]=d.get(a[r],0)+1

    if r-l+1>k:
        d[a[l]]-=1
        if d[a[l]]==0:
            del d[a[l]]
        l+=1

    if r-l+1==k:
        m=max(m,len(d))

print(m)

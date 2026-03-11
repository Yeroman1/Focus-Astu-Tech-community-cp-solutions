n,h=map(int, input().split())
fr=list(map(int, input().split()))
width=0
for p in fr:
    if p>h:
        width+=2
    else:
        width+=1
print(width)

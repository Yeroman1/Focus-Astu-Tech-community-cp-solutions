n=int(input())
a=list(map(int, input().split()))
q=int(input())

for i in range(q):
  s=list(map(int, input().split()))
  if len(s)==2:
    print(a[s[1]-1])
  else:
    a[s[1]-1]=s[2]

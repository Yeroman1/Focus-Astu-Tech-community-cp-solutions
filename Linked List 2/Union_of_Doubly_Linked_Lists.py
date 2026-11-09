class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

n=int(input())

nodes=[None]+[Node(i) for i in range(1,n+1)]

for i in range(1,n+1):
    left,right=map(int,input().split())

    if left:
        nodes[i].prev=nodes[left]

    if right:
        nodes[i].next=nodes[right]

starts=[]

for i in range(1,n+1):
    if nodes[i].prev==None:
        starts.append(nodes[i])

for i in range(len(starts)-1):
    a=starts[i]

    while a.next!=None:
        a=a.next

    b=starts[i+1]

    a.next=b
    b.prev=a

for i in range(1,n+1):
    p=nodes[i].prev
    q=nodes[i].next

    print(p.val if p else 0,q.val if q else 0)

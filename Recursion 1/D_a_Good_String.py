def solve(s, c):
    if len(s)==1:
        return 0 if s==c else 1

    m=len(s)//2
    left=s[:m]
    right=s[m:]

    x=0 
    for i in left:
        if i!=c:
            x+=1

    y=0
    for i in right:
        if i!=c:
            y+=1

    cost1=x+solve(right, chr(ord(c)+1))
    cost2=y+solve(left, chr(ord(c)+1))
    return min(cost1, cost2)
for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s, 'a'))
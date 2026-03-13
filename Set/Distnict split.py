t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    p = [0]*n
    a = set()

    for i in range(n):
        a.add(s[i])
        p[i] = len(a)

    q = [0]*n
    b = set()

    for i in range(n-1, -1, -1):
        b.add(s[i])
        q[i] = len(b)

    r = 0
    for i in range(n-1):
        r = max(r, p[i] + q[i+1])

    print(r)

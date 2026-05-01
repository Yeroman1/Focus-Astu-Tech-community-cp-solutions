t = int(input())

for i in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))

    ans = float('inf')

    for i in range(n - d + 1):
        w = a[i:i+d]
        ans = min(ans, len(set(w)))

    print(ans)

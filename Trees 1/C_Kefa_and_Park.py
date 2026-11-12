n, m = map(int, input().split())
cats = [0] + list(map(int, input().split()))

adj = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

ans = 0
stack = [(1, 0, cats[1])]

while stack:
    node, parent, streak = stack.pop()

    if streak > m:
        continue

    is_leaf = True
    for neighbor in adj[node]:
        if neighbor != parent:
            is_leaf = False
            next_streak = streak + 1 if cats[neighbor] == 1 else 0
            stack.append((neighbor, node, next_streak))

    if is_leaf and node != 1:
        ans += 1

print(ans)
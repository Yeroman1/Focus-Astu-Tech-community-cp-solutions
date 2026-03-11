n = int(input())
c = 0

for _ in range(n):
    x, y, z = map(int, input().split())
    if x + y + z > 1:
        c += 1

print(c)

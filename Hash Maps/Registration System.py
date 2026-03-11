n = int(input())
d = {}

for _ in range(n):
    s = input().strip()
    
    if s not in d:
        d[s] = 1
        print("OK")
    else:
        t = s + str(d[s])
        print(t)
        d[s] += 1
        d[t] = 1

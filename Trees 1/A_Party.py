n = int(input())

manager = [0] * (n + 1)

for i in range(1, n + 1):
    manager[i] = int(input())

answer = 0

for i in range(1, n + 1):
    count = 1
    current = i

    while manager[current] != -1:
        current = manager[current]
        count += 1

    answer = max(answer, count)

print(answer)
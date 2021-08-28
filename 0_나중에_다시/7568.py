# 덩치

n = int(input())
total = []

for _ in range(n):
    a, b = map(int, input().split())
    total.append((a, b))

for i in total:
    rank = 1
    for j in total:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

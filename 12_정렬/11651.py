# 좌표 정렬하기2

n = int(input())
answer = []

for _ in range(n):
    a, b = map(int, input().split())
    answer.append((a, b))

answer.sort(key=lambda x: (x[1], x[0]))

for i in range(len(answer)):
    print(answer[i][0], answer[i][1])

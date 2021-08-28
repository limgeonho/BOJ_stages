# 직사각형 네개의 합집합의 면적 구하기

answer = 0

board = [[0] * 101 for _ in range(101)]
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            board[i][j] = 1

for i in range(101):
    for j in range(101):
        if board[i][j] != 0:
            answer += 1

print(answer)

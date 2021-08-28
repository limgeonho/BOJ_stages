# 종이 자르기

n = int(input())
board = [[0]*1001 for _ in range(1001)]
for color in range(1, n+1):
    a, b, c, d = map(int, input().split())
    for i in range(a, a+c):
        for j in range(b, b+d):
            board[i][j] = color

for color in range(1, n+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == color:
                cnt += 1
    print(cnt)

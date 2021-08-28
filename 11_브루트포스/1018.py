# 체스판 다시 칠하기

def check(words):
    chess_1 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'
    chess_2 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'

    cnt_1 = 0
    cnt_2 = 0
    for i in range(64):
        if words[i] != chess_1[i]:
            cnt_1 += 1

    for i in range(64):
        if words[i] != chess_2[i]:
            cnt_2 += 1
    final = min(cnt_1, cnt_2)
    return final


n, m = map(int, input().split())
chess = []

for _ in range(n):
    chess.append(input())
answer = []

for i in range(n-8+1):
    for j in range(m-8+1):
        cut = ''
        for k in range(8):
            for l in range(8):
                cut += chess[i+k][j+l]
        answer.append(check(cut))

min_num = min(answer)
print(min_num)

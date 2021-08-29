# 빙고
import sys
sys.stdin = open('input.txt')


def check_bingo_row(array, cnt):
    for row in array:
        if sum(row) == 0:
            cnt += 1
    return cnt


def check_bingo_col(array, cnt):
    tmp = list(zip(*array))
    for row in tmp:
        if sum(row) == 0:
            cnt += 1
    return cnt

def check_bingo_cross(array, cnt):
    tmp_1 = 0
    tmp_2 = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                tmp_1 += array[i][j]
    if tmp_1 == 0:
        cnt += 1

    for i in range(5):
        for j in range(5):
            if i + j == 4:
                tmp_2 += array[i][j]
    if tmp_2 == 0:
        cnt += 1
    return cnt


bingo = [list(map(int, input().split())) for _ in range(5)]

answer = []
cnt = 0
for _ in range(5):
    answer.extend(list(map(int, input().split())))

for k in range(len(answer)):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == answer[k]:
                bingo[i][j] = 0
                if k > 10:
                    cnt = check_bingo_row(bingo, cnt)
                    cnt = check_bingo_col(bingo, cnt)
                    cnt = check_bingo_cross(bingo, cnt)
                    if cnt >= 3:
                        print(k)
                        break

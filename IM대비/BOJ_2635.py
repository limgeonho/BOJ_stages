# 수 이어가기

n = int(input())
length = 0
answer = []
for i in range(n+1):
    cnt = 0
    tmp = [n, i]
    while True:
        next_num = tmp[cnt] - tmp[cnt+1]
        if next_num < 0:
            break
        tmp.append(next_num)
        if length < len(tmp):
            length = len(tmp)
            answer = tmp[:]
        cnt += 1


print(length)
print(*answer)

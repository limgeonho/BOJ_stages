# 분해합

n = int(input())

for i in range(1, n+1):
    tmp = list(map(int, str(i)))
    answer = i + sum(tmp)
    if answer == n:
        print(i)
        break
else:
    print(0)

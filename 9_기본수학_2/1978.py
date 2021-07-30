# 소수 찾기

n = int(input())

arr = list(map(int, input().split()))
cnt = 0
for x in arr:
    if x == 1:
        continue
    else:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            cnt += 1
print(cnt)

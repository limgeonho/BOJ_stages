# 한수

n = int(input())
cnt = 0


if n < 100:
    cnt = n
elif 100 <= n <= 1000:
    arr = list(range(100, n+1))
    cnt = 99
    for x in arr:
        if x == 1000:
            continue
        if (int(str(x)[2]) - int(str(x)[1])) == (int(str(x)[1]) - int(str(x)[0])):
            cnt += 1
        else:
            continue

print(cnt)

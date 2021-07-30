# 소수

m = int(input())
n = int(input())

arr = []
for num in range(m, n+1):
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        arr.append(num)
if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))

# 더하기 사이클

n = int(input())
cnt = 0
target = n
while True:
    tmp = (n//10) + (n % 10)
    if tmp >= 10:
        nextNum = (n % 10)*10 + (tmp % 10)
        cnt += 1
    else:
        nextNum = (n % 10)*10 + tmp
        cnt += 1
    n = nextNum
    if nextNum == target:
        break
print(cnt)

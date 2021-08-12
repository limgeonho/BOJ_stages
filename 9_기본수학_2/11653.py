# 소인수분해

n = int(input())

answer = []
tmp = 2
while True:
    if n == 1:
        break

    while True:
        if n % tmp != 0:
            break
        if n % tmp == 0:
            answer.append(tmp)
            n = n // tmp
    tmp += 1

for i in answer:
    print(i)


# N = int(input())

# for i in range(2, int(N ** 0.5) + 1):
#     while N % i == 0:
#         print(i)
#         N //= i

# if N > 1:
#     print(N)

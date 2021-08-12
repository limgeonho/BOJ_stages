# 소수 구하기
import math


def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)

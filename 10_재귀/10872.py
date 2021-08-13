# 팩토리얼
import math

N = int(input())
print(math.factorial(N))


def fac(x):
    if x == 1:
        return 1
    else:
        return x * fac(x-1)


print(fac(N))

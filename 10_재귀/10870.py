# 피보나치 수

n = int(input())


def fiv(x):
    if x == 1 or x == 0:
        return x
    else:
        return fiv(x-1) + fiv(x-2)


print(fiv(n))

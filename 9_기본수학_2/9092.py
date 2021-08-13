# 골드바흐의 추측

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


T = int(input())
answer = []
for _ in range(T):
    n = int(input())
    for i in range(n//2, 0, -1):
        tmp = n - i
        if isPrime(i) and isPrime(tmp):
            answer.append((i, tmp))
            print(i, tmp)
            break

# 베르트랑 공준

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


numbers = list(range(2, 123456*2+1))
prime_numbers = []
for i in numbers:
    if isPrime(i):
        prime_numbers.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in prime_numbers:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)

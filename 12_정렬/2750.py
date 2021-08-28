# 수 정렬하기

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

for i in range(len(numbers)):
    print(numbers[i])

import sys
from bisect import bisect_left
# 수 정렬하기3

n = int(input())
numbers = []
for _ in range(n):
    tmp = int(input())
    place = bisect_left(numbers, tmp)
    numbers.insert(place, tmp)

for i in range(len(numbers)):
    print(numbers[i])

# 메모리 초과... 이런방법이...!!

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

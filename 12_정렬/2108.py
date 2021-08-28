# 통계학
from collections import Counter
n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
length = len(numbers)

first = sum(numbers) / length
second = numbers[length//2]

counter = Counter(numbers)
# print(dict(counter))
frequent_nums = []
frequent = counter.most_common(1)

for k, v in counter.items():
    if v == frequent[0][1]:
        frequent_nums.append(k)

print(f'{first:.0f}')

print(second)

if len(frequent_nums) > 1:
    print(frequent_nums[1])
else:
    print(frequent_nums[0])

print(max(numbers) - min(numbers))

# 셀프 넙버

numbers = set(range(1, 10001))
check_numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    check_numbers.add(i)

answer = list(numbers - check_numbers)
answer.sort()

for num in answer:
    print(num)

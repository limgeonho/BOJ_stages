# 숫자의 개수

answer = 1
for _ in range(3):
    answer *= int(input())

for i in range(0, 10):
    print(str(answer).count(str(i)))

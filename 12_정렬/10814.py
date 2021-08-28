# 나이순 정렬

n = int(input())
answer = []


for _ in range(n):
    age, name = map(str, input().split())
    answer.append((age, name))

answer.sort(key=lambda x: int(x[0]))

for s in answer:
    print(s[0], s[1])

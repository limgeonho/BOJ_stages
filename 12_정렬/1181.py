# 단어 정렬

n = int(input())
answer = []

for _ in range(n):
    answer.append(input())

tmp = set(answer)

answer = list(tmp)

answer.sort(key=lambda s: (len(s), s))

for s in answer:
    print(s)

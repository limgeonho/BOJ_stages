# 나머지

answer = []

for _ in range(10):
    answer.append(int(input()) % 42)

setAnswer = set(answer)
print(len(setAnswer))

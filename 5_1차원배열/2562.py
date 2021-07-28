# 최댓값

answer = []
for _ in range(9):
    answer.append(int(input()))

mNum = max(answer)
for i in range(9):
    if answer[i] == mNum:
        print(mNum)
        print(i+1)

arr = [int(input()) for _ in range(9)]
print(max(arr), arr.index(max(arr))+1)

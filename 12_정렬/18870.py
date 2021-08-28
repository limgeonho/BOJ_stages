# 좌표 압축

from types import new_class


n = int(input())
answer = []

array = list(map(int, input().split()))

tmp = array[:]
tmp = set(tmp)
tmp = list(tmp)
tmp.sort()
num_dict = {}
for i in range(len(tmp)):
    num_dict[tmp[i]] = i

for a in array:
    print(num_dict[a], end=' ')

# 시간초과
# for num in array:
#     print(tmp.index(num), end=' ')


# for i in range(n):
#     cnt = 0
#     for j in range(n):
#         if array[i] > array[j]:
#             cnt += 1
#     answer.append(cnt)

# print(*answer)

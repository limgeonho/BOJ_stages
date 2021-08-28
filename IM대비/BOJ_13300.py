# 방 배정
from math import ceil

N, K = map(int, input().split())
students_info = [[0, 0] for _ in range(7)]
rooms = 0

for _ in range(N):
    gender, grade = map(int, input().split())
    students_info[grade][gender] += 1

for student in students_info:
    for i in range(2):
        if student[i] == 0:
            continue
        else:
            tmp = ceil(student[i] / K)
            if tmp < 1:
                rooms += 1
            else:
                rooms += tmp
print(rooms)

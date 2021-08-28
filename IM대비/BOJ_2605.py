# 줄 세우기

n = int(input())

line = list(map(int, input().split()))

students = []

for i in range(len(line)):
    students.insert(len(students)-line[i], i+1)
print(*students)

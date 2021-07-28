# X 보다 작은 수
import sys

n, x = map(int, input().split())

answer = map(int, sys.stdin.readline().split())
for num in answer:
    if x > num:
        print(num, end=' ')

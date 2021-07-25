# 두 수 비교하기

n, m = map(int, input().split())

if n > m:
    print('>')
elif n < m:
    print('<')
else:
    print('==')

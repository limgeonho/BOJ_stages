# 알람시계

h, m = map(int, input().split())

if m >= 45:
    print(h, end=' ')
    print(m-45)
elif m < 45:
    m = 60 - (45-m)
    if h == 0:
        h = 23
    else:
        h -= 1
    print(h, end=' ')
    print(m)

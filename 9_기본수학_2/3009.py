# 네 번째 점


a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
ans1 = ans2 = 0
if a == c:
    if b == f:
        ans2 = d
    else:
        ans2 = b
    ans1 = e

if a == e:
    if b == d:
        ans2 = f
    else:
        ans2 = b
    ans1 = c

if c == e:
    if d == b:
        ans2 = f
    else:
        ans2 = d
    ans1 = a

print(ans1, ans2)

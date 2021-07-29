# 문자열 반복

t = int(input())
for _ in range(t):
    r, s = map(str, input().split())
    answer = ''
    for char in s:
        answer += (char*int(r))
    print(answer)
